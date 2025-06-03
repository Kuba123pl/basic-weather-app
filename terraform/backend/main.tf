terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=4.0.0"
    }
  }
}
provider "azurerm" {
    subscription_id = var.sub_id
  features {}
}
resource "azurerm_resource_group" "RG_backend" {
  name = "RG_backend"
  location = var.region
}
resource "azurerm_container_app_environment" "container_environment" {
  name                       = "containerApp-Environment"
  location                   = azurerm_resource_group.RG_backend.location
  resource_group_name        = azurerm_resource_group.RG_backend.name
}

resource "azurerm_container_app" "api_container_app" {
  name = "apicontainerapp"
  resource_group_name = azurerm_resource_group.RG_backend.name
  container_app_environment_id = azurerm_container_app_environment.container_environment.id
  revision_mode = "Single"
 template {
    container {
      name = "example"
      image = "mcr.microsoft.com/azuredocs/containerapps-helloworld:latest"
      cpu    = 0.5
      memory = "1.0Gi"
    }
    max_replicas = 2
    min_replicas = 0
 } 
}
resource "azurerm_container_registry" "container_registry" {
  name = "containerRegistryjb69"
  resource_group_name = azurerm_resource_group.RG_backend.name
  location = azurerm_resource_group.RG_backend.location
  sku = "Basic"
  admin_enabled = true
}