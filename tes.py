from telethon import *
from CloudFlare import CloudFlare

# Replace with your API credentials
api_id = '6'
api_hash = 'eb06d4abfb49dc3eeb1aeb98ae0f581e'
bot_token = '7467941614:AAH3KMkNugkLcWVNT5SMF60iz2lFBXDl1Es'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
cf = CloudFlare(email='dakross81@gmail.com', token='d0328b30f47965ece4e692b1c0c3dc55ac224')
# Domain and ZoneID variables
DOMAIN1 = 'efwangstore.my.id'
ZONEID1 = '674bd9c87f757f2ab1f5254c0146fc56'
DOMAIN2 = 'premiumserver.me'
ZONEID2 = '24900651852c5783074d7a2bfecd7a29'
DOMAIN3 = 'fonestores.my.id'
ZONEID3 = 'd39d6d776279cea12773883d5a7e0362'
DOMAIN4 = 'example4.com'
ZONEID4 = 'your_zone_id_4'

GARISATAS = '┏━━━━━━━━━━━━━━━━━━━━┓'
GARISTENGAH   = '┣━━━━━━━━━━━━━━━━━━━━┫'
GARISBAWAH  = '┗━━━━━━━━━━━━━━━━━━━━┛'

CHAT_ID = [5066246825]  # Replace with allowed chat IDs
user_states = {}
WAIT_DOMAIN, WAIT_SUBDOMAIN = 1, 2

def reset_state(user_id):
    if user_id in user_states:
        del user_states[user_id]

@client.on(events.NewMessage(pattern='/add_ip2'))
@client.on(events.CallbackQuery)
@client.on(events.NewMessage)
async def add_ip2(event):
    user_id = event.chat_id

    async def add_record(user_id, domain, zone_id, sub, content):
        record = {
            'type': 'A',
            'name': sub,
            'content': content,
        }
        try:
            records = cf.zones.dns_records.get(zone_id, params={'name': f"{sub}.{domain}"})
            if records:
                previous_ip = records[0]['content']
                cf.zones.dns_records.delete(zone_id, records[0]['id'])
                message = f"""
{GARISATAS}
          **Hapus Domain Berhasil**
{GARISTENGAH}
  `Name   : ``{sub}`
  `Sub    : ``{sub}.{domain}`
  `IP     : ``{previous_ip}`
  `Domain : ``{domain}`
{GARISBAWAH} 
"""
                await client.send_message(user_id, message)
            
            cf.zones.dns_records.post(zone_id, data=record)
            message = f"""
{GARISATAS}
                 **Add IP Berhasil**
{GARISTENGAH}
  `Name   : ``{sub}`
  `Sub    : ``{sub}.{domain}`
  `IP     : ``{content}`
  `Domain : ``{domain}`
{GARISBAWAH} 
"""
            await client.send_message(user_id, message)
        except Exception as e:
            await client.send_message(user_id, f"Error: {e}")

    if isinstance(event, events.NewMessage.Event) and event.pattern_match:
        if user_id not in CHAT_ID:
            await event.reply("Akses ditolak❌")
            return
        
        buttons = [
            [Button.inline(DOMAIN1, b'domain1'), Button.inline(DOMAIN2, b'domain2')],
            [Button.inline(DOMAIN3, b'domain3'), Button.inline(DOMAIN4, b'domain4')],
            [Button.inline('Cancel', b'cancel')]
        ]
        user_states[user_id] = WAIT_DOMAIN
        await event.respond('Pilih domain:', buttons=buttons)

    elif isinstance(event, events.CallbackQuery.Event):
        data = event.data.decode('utf-8')
        
        if user_states.get(user_id) == WAIT_DOMAIN:
            if data == 'cancel':
                reset_state(user_id)
                await event.edit("**Operasi dibatalkan**")
                return
            
            domain_index = int(data[-1])
            domain = eval(f"DOMAIN{domain_index}")
            zone_id = eval(f"ZONEID{domain_index}")
            user_states[user_id] = {'state': WAIT_SUBDOMAIN, 'domain': domain, 'zone_id': zone_id}
            
            await event.respond(f"**Input subdomain dan IP: <sub> <ip>**")
        elif data == 'cancel':
            reset_state(user_id)
            await event.edit("**Operasi dibatalkan**")
        
    elif isinstance(event, events.NewMessage.Event):
        if user_id not in CHAT_ID:
            return
        
        state_info = user_states.get(user_id)
        if not state_info:
            return
        
        if state_info['state'] == WAIT_SUBDOMAIN:
            parts = event.message.text.split()
            if len(parts) < 2:
                await event.respond("**Format tidak valid. Harap input subdomain dan IP**")
                return
            
            sub = parts[0]
            content = parts[1]
            domain = state_info['domain']
            zone_id = state_info['zone_id']
            
            await add_record(user_id, domain, zone_id, sub, content)
            reset_state(user_id)
 
@client.on(events.NewMessage(pattern='/add_publik'))
@client.on(events.CallbackQuery)
@client.on(events.NewMessage)
async def add_ip2(event):
    user_id = event.chat_id

    async def add_record(user_id, domain, zone_id, sub, content):
        record = {
            'type': 'CNAME',
            'name': sub,
            'content': content,
        }
        try:
            records = cf.zones.dns_records.get(zone_id, params={'name': f"{sub}.{domain}"})
            if records:
                previous_ip = records[0]['content']
                cf.zones.dns_records.delete(zone_id, records[0]['id'])
                message = f"""
{GARISATAS}
          **Hapus Domain Berhasil**
{GARISTENGAH}
  `Name   : ``{sub}`
  `Sub    : ``{sub}.{domain}`
  `IP     : ``{previous_ip}`
  `Domain : ``{domain}`
{GARISBAWAH} 
"""
                await client.send_message(user_id, message)
            
            cf.zones.dns_records.post(zone_id, data=record)
            message = f"""
{GARISATAS}
                 **Add IP Berhasil**
{GARISTENGAH}
  `Name   : ``{sub}`
  `Sub    : ``{sub}.{domain}`
  `IP     : ``{content}`
  `Domain : ``{domain}`
{GARISBAWAH} 
"""
            await client.send_message(user_id, message)
        except Exception as e:
            await client.send_message(user_id, f"Error: {e}")

    if isinstance(event, events.NewMessage.Event) and event.pattern_match:
        if user_id not in CHAT_ID:
            await event.reply("Akses ditolak❌")
            return
        
        buttons = [
            [Button.inline(DOMAIN1, b'domain1'), Button.inline(DOMAIN2, b'domain2')],
            [Button.inline(DOMAIN3, b'domain3'), Button.inline(DOMAIN4, b'domain4')],
            [Button.inline('Cancel', b'cancel')]
        ]
        user_states[user_id] = WAIT_DOMAIN
        await event.respond('Pilih domain:', buttons=buttons)

    elif isinstance(event, events.CallbackQuery.Event):
        data = event.data.decode('utf-8')
        
        if user_states.get(user_id) == WAIT_DOMAIN:
            if data == 'cancel':
                reset_state(user_id)
                await event.edit("**Operasi dibatalkan**")
                return
            
            domain_index = int(data[-1])
            domain = eval(f"DOMAIN{domain_index}")
            zone_id = eval(f"ZONEID{domain_index}")
            user_states[user_id] = {'state': WAIT_SUBDOMAIN, 'domain': domain, 'zone_id': zone_id}
            
            await event.respond(f"**Input subdomain dan domain<sub> <domain>**")
        elif data == 'cancel':
            reset_state(user_id)
            await event.edit("**Operasi dibatalkan**")
        
    elif isinstance(event, events.NewMessage.Event):
        if user_id not in CHAT_ID:
            return
        
        state_info = user_states.get(user_id)
        if not state_info:
            return
        
        if state_info['state'] == WAIT_SUBDOMAIN:
            parts = event.message.text.split()
            if len(parts) < 2:
                await event.respond("**Format tidak valid. Harap input subdomain dan IP**")
                return
            
            sub = parts[0]
            content = parts[1]
            domain = state_info['domain']
            zone_id = state_info['zone_id']
            
            await add_record(user_id, domain, zone_id, sub, content)
            reset_state(user_id)            
       
client.run_until_disconnected()
