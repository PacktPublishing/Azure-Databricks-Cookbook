$appId=""
$appSecret=""
$tenantId=""
$subscriptionName=""
$resourceGroup = "CookbookRG"

az login --service-principal --username $appId --password $appSecret --tenant $TenantId

az account set --subscription $subscriptionName

az group create --name $resourceGroup --location "East US"

az databricks workspace create --resource-group $resourceGroup --name BigDataWorkspace --location "East US" --sku standard