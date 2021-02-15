# Change the APPId, AppSecret, TenantId, SubscriptionName and ResourceGroup Name
$appId="1asddasdasd1a7-f7ce-44dada7-b4eb-4esdasdsd65a6"
$appSecret="sdasdd8dasda5j_3VsdasdasdKw~.Ssdasdadasd~d"
$tenantId="asdad8bf-8sdads1-412dqw-9asdadb-asdasdasdab47"
$subscriptionName="Pay As you Go"
$resourceGroup = "CookbookRG"

az login --service-principal --username $appId --password $appSecret --tenant $TenantId

az account set --subscription $subscriptionName

az group deployment create --resource-group $resourceGroup `
--template-file azuredeploy.json --parameters azuredeploy.parameters.json
