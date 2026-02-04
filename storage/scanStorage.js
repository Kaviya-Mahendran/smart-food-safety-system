// storage/scanStorage.js
import { StorageService } from "./storageService.js";

const NAMESPACE = "label_scans";

export function saveScanResult(scanId, payload) {
  return StorageService.write(NAMESPACE, scanId, {
    scanId,
    scannedAt: new Date().toISOString(),
    ...payload
  });
}

export function getScanResult(scanId) {
  return StorageService.read(NAMESPACE, scanId);
}

export function deleteScanResult(scanId) {
  return StorageService.delete(NAMESPACE, scanId);
}
