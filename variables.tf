variable "org_id" {
  type        = string
  description = "Numeric organization ID"
}

variable "project_id" {
  type        = string
  description = "Project ID to deploy Function into"
}

variable "region" {
  type        = string
  description = "Region for deploying Function"
  default     = "us-central1"
}

variable "feed_id" {
  type        = string
  description = "Name of the Asset Inventory Feed"
  default     = "org_ai_feed_networktag"
}
