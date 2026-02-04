import { saveScanResult, getScanResult } from "./storage/scanStorage.js";
import { saveFreshnessScore, getFreshnessScore } from "./storage/freshnessStorage.js";

console.log("Running storage test...");

// Save scan
saveScanResult("scan_001", {
  ocrText: "Contains milk and nuts",
  allergensDetected: ["milk", "nuts"],
  expiryDate: "2026-02-10",
  riskLevel: "high"
});

// Read scan
console.log("Scan result:", getScanResult("scan_001"));

// Save freshness score
saveFreshnessScore("milk_123", {
  score: 0.82,
  status: "safe",
  modelVersion: "v1.0.0"
});

// Read freshness score
console.log("Freshness score:", getFreshnessScore("milk_123"));
