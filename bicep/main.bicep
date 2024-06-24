param acrName string
param clusterName string
param kvName string

module acrModule 'ContainerRegistry.bicep' = {
  name: 'acrDeploy'
  params: {
    acrName: acrName
  }
}

module aksModule 'Kubernetes.bicep' = {
  name: 'aksDeploy'
  params: {
    clusterName: clusterName
    dnsPrefix: clusterName
    linuxAdminUsername: 'UserAdmin'
    sshRSAPublicKey: 'ssh-rsa AAAA'
    istioServiceMeshEnabled: true
    istioIngressGatewayEnabled: true
    openServiceMeshEnabled: false
    httpApplicationRoutingEnabled: true
    daprEnabled: true
    kedaEnabled: true
    daprHaEnabled: true
    verticalPodAutoscalerEnabled: true
  }
}

var secrets =  {
  secrets: [
    {
      secretName: 'Secret01'
      secretValue: 'Value01'
    }
  ]
}

module keyVaultModule 'KeyVault.bicep' = {
  name: 'keyVaultDeploy'
  params: {
    keyVaultName: kvName
    objectId: '051c760b-9769-4f0f-9828-09197ff28b7c'
    secretsObject: secrets
  }
}
