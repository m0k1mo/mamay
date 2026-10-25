// Mamay Native — GPU probe on GitHub macOS runners (Розробка #1, 25.10.2026)
import Foundation
import Metal

func out(_ s: String) { print(s); fflush(stdout) }
out("macOS: \(ProcessInfo.processInfo.operatingSystemVersionString)")
guard let d = MTLCreateSystemDefaultDevice() else { out("RESULT: NO METAL DEVICE"); exit(0) }
out("device: \(d.name)  unified: \(d.hasUnifiedMemory)  lowPower: \(d.isLowPower)")
let fams: [(String, MTLGPUFamily)] = [("apple5", .apple5), ("apple6", .apple6), ("apple7", .apple7), ("apple8", .apple8),
  ("apple9", .apple9), ("apple10", .apple10), ("mac2", .mac2), ("metal3", .metal3)]
for (n, f) in fams { out("family \(n): \(d.supportsFamily(f))") }
if #available(macOS 26.0, *) { out("family metal4: \(d.supportsFamily(.metal4))") }
out("maxThreadgroupMemory: \(d.maxThreadgroupMemoryLength)")
out("maxThreadsPerThreadgroup: \(d.maxThreadsPerThreadgroup)")
out("readWriteTextureTier: \(d.readWriteTextureSupport.rawValue)")
out("recommendedMaxWorkingSet MB: \(d.recommendedMaxWorkingSetSize / 1_048_576)")
out("maxBufferLength MB: \(d.maxBufferLength / 1_048_576)")
out("sparseTileSizeInBytes: \(d.sparseTileSizeInBytes)")
out("supports32BitFloatFiltering: \(d.supports32BitFloatFiltering)")
out("supportsRaytracing: \(d.supportsRaytracing)")
out("timestampAtStageBoundary: \(d.supportsCounterSampling(.atStageBoundary))")
if #available(macOS 26.0, *) {
  if #available(macOS 26.4, *) { out("supportsPlacementSparse: \(d.supportsPlacementSparse)") }
  if let q = d.makeMTL4CommandQueue() { out("MTL4CommandQueue: OK \(q)") } else { out("MTL4CommandQueue: nil") }
}

// compute smoke: runtime-compiled kernel, 256x256 float texture, compare with CPU
let src = """
#include <metal_stdlib>
using namespace metal;
kernel void k(texture2d<float, access::write> o [[texture(0)]], uint2 g [[thread_position_in_grid]]) {
  if (g.x >= o.get_width() || g.y >= o.get_height()) return;
  float v = sin(float(g.x) * 0.05) * cos(float(g.y) * 0.07);
  o.write(float4(v, v * 0.5, 1.0 - v, 1.0), g);
}
kernel void ssum(device float* o [[buffer(0)]], uint i [[thread_position_in_grid]]) {
  o[i] = simd_sum(float(i));
}
"""
do {
  let lib = try d.makeLibrary(source: src, options: nil)
  let pso = try d.makeComputePipelineState(function: lib.makeFunction(name: "k")!)
  out("pso: threadExecutionWidth \(pso.threadExecutionWidth) maxTotal \(pso.maxTotalThreadsPerThreadgroup)")
  let W = 256
  let td = MTLTextureDescriptor.texture2DDescriptor(pixelFormat: .rgba32Float, width: W, height: W, mipmapped: false)
  td.usage = [.shaderWrite, .shaderRead]; td.storageMode = .shared
  let tex = d.makeTexture(descriptor: td)!
  let q = d.makeCommandQueue()!
  let cb = q.makeCommandBuffer()!
  let e = cb.makeComputeCommandEncoder()!
  e.setComputePipelineState(pso); e.setTexture(tex, index: 0)
  e.dispatchThreads(MTLSize(width: W, height: W, depth: 1), threadsPerThreadgroup: MTLSize(width: pso.threadExecutionWidth, height: 8, depth: 1))
  e.endEncoding()
  let t0 = Date(); cb.commit(); cb.waitUntilCompleted()
  out("compute status: \(cb.status.rawValue) error: \(String(describing: cb.error)) time ms: \(Int(Date().timeIntervalSince(t0) * 1000)) gpu ms: \((cb.gpuEndTime - cb.gpuStartTime) * 1000)")
  var px = [Float](repeating: 0, count: W * W * 4)
  tex.getBytes(&px, bytesPerRow: W * 16, from: MTLRegionMake2D(0, 0, W, W), mipmapLevel: 0)
  var maxErr: Float = 0
  for y in 0..<W { for x in 0..<W { let v = sin(Float(x) * 0.05) * cos(Float(y) * 0.07); maxErr = max(maxErr, abs(px[(y * W + x) * 4] - v)) } }
  out("compute vs CPU max error: \(maxErr)")
  do {
    let p2 = try d.makeComputePipelineState(function: lib.makeFunction(name: "ssum")!)
    let b = d.makeBuffer(length: 64 * 4, options: .storageModeShared)!
    let c2 = q.makeCommandBuffer()!; let e2 = c2.makeComputeCommandEncoder()!
    e2.setComputePipelineState(p2); e2.setBuffer(b, offset: 0, index: 0)
    e2.dispatchThreads(MTLSize(width: 64, height: 1, depth: 1), threadsPerThreadgroup: MTLSize(width: 32, height: 1, depth: 1))
    e2.endEncoding(); c2.commit(); c2.waitUntilCompleted()
    let r = b.contents().bindMemory(to: Float.self, capacity: 64)
    out("simd_sum: status \(c2.status.rawValue) first \(r[0]) (expect 496) second-group \(r[32]) (expect 1520)")
  } catch { out("simd_sum: FAILED \(error)") }
} catch { out("compute: FAILED \(error)") }
out("RESULT: done")
