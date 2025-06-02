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

#Basic web_app

resource "azurerm_resource_group" "RG_Frontend" {
    name = "RG_Frontend"
    location = var.region
}

resource "azurerm_service_plan" "SP1" {
  name = "service_plan1"
  location = azurerm_resource_group.RG_Frontend.location
  resource_group_name = azurerm_resource_group.RG_Frontend.name
  os_type = "Linux"
  sku_name = "B1"
}


resource "azurerm_linux_web_app" "main_WebApp" {
    name = "mainWebApp"
    location = azurerm_resource_group.RG_Frontend.location
    service_plan_id = azurerm_service_plan.SP1.id
    resource_group_name = azurerm_resource_group.RG_Frontend.name
    site_config {}
}