resource "azurerm_resource_group" "rg" {
  name     = "AzFunctionak-rg"
  location = "centralus"
}

resource "azurerm_storage_account" "sa" {
  name                     = "azfunctionaksa"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_service_plan" "example" {
  name                = "Python-app-service-plan"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_function_app" "example" {
  name                = "AzFunctionak"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  storage_account_name       = azurerm_storage_account.sa.name
  storage_account_access_key = azurerm_storage_account.sa.primary_access_key
  service_plan_id            = azurerm_service_plan.example.id

  site_config {
   application_stack {
        python_version = "3.8"
   }    
  }
}