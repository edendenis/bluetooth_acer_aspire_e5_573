#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `Bluetooth do Acer Aspire E5-573` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/configurar/usar o `Bluetooth do Acer Aspire E5-573` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/use the `Bluetooth Acer Aspire E5-573` on `Linux Ubuntu`._

# ## Revisão(ões)/Versão(ões)

# |Revisão número|Data da revisão|Descrição da revisão|Autor da revisão|
# |:-:|:-:|:-|:-|
# |0|03/10/2023|<ul><li>Revisão inicial/criação do documento.</li></ul>|Eden Denis F. da S. L. Santos|

# ## Descrição [2]
# 
# ### `bluetooth`
# 
# O Bluetooth é uma tecnologia de comunicação sem fio de curto alcance amplamente utilizada para a interconexão de dispositivos eletrônicos, como smartphones, tablets, fones de ouvido, teclados, mouses e muitos outros. Essa tecnologia permite a transferência de dados e áudio entre dispositivos próximos, geralmente dentro de um raio de alguns metros. O Bluetooth é conhecido por sua conveniência e facilidade de uso, permitindo que os dispositivos se conectem automaticamente e compartilhem informações de forma eficiente. É amplamente utilizado em dispositivos móveis e acessórios, bem como em sistemas de áudio para streaming de música sem fio e em dispositivos de automação residencial para controlar aparelhos e equipamentos remotamente. Com suas várias versões e aprimoramentos ao longo dos anos, o Bluetooth se tornou uma tecnologia essencial para a conectividade sem fio em muitos aspectos de nossas vidas cotidianas.
# 

# ## 1. Resolvendo Problemas de `Bluetooth no Acer Aspire E5-573` no `Linux Ubuntu` [1]
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes APT. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo APT e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# 3. **Instale os pacotes de firmware:** Instale os pacotes `linux-firmware` e `linux-firmware-atheros` usando o gerenciador de pacotes `apt`.
# 
#     ```
#     sudo apt install linux-firmware
#     # sudo apt install linux-firmware-atheros
#     ```
# 
# 4. **Blacklist do módulo `acer-wmi`:** Crie um arquivo de configuração para colocar o módulo acer-wmi na lista negra (blacklist). Abra o arquivo em um editor de texto como o nano: `sudo nano /etc/modprobe.d/acer-wmi.conf`
# 
#     4.1 **Adicione a seguinte linha ao arquivo e salve:** `blacklist acer-wmi`
# 
# Salve o arquivo e saia do editor (`Ctrl+O` para salvar, `Ctrl+X` para sair no `nano`).
# 
# 5. **Reinicie o sistema:** Reinicie o sistema para aplicar todas as mudanças. `sudo reboot
# `
# Depois de seguir esses passos, o Bluetooth deve funcionar corretamente no seu notebook `Acer Aspire E5-573` rodando `Linux Ubuntu`.
# 
# Espero que isso ajude você a documentar o processo!

# ## Referências
# 
# [1] OPENAI. ***Bluetooth não funciona - resolvido.*** Disponível em: <https://chat.openai.com/c/0d5b6ae2-3dcc-4cd9-92b1-5efc19174ca4> (texto adaptado). Acessado em: 20/10/2023 00:55.
# 
# [2] OPENAI. ***VS code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 15/11/2023 16:26.
# 
