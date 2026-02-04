// storage/freshnessStorage.js
import { StorageService } from "./storageService.js";

const NAMESPACE = "freshness_scores";

export function saveFreshnessScore(itemId, scoreData) {
  return StorageService.write(NAMESPACE, itemId, {
    itemId,
    calculatedAt: new Date().toISOString(),
    ...scoreData
  });
}

export function getFreshnessScore(itemId) {
  return StorageService.read(NAMESPACE, itemId);
}
