from pywa import WhatsApp
## token : EAATYGW2lhwgBQ4NNpLFVOzkhBCfH7SeWuus3RkF47cq9ldlK7QnU9UHhYZAH9xfWlOnf6p3sbbZAZC179mGXxiS6ZBLRt0EU5bWPrkjLOsjP1mAWVrPR8xadDOnEOWDuyhD0SFhojrOpqcKoo68NzqNdtJMGNqdoKEAZCGP1xdD1EMVn6J2CY86XZCWe30HQZDZD
# cria cliente
wa = WhatsApp(
    phone_id="954435134428733",  # coloque aqui o PHONE NUMBER ID real
    token="EAATYGW2lhwgBQ4NNpLFVOzkhBCfH7SeWuus3RkF47cq9ldlK7QnU9UHhYZAH9xfWlOnf6p3sbbZAZC179mGXxiS6ZBLRt0EU5bWPrkjLOsjP1mAWVrPR8xadDOnEOWDuyhD0SFhojrOpqcKoo68NzqNdtJMGNqdoKEAZCGP1xdD1EMVn6J2CY86XZCWe30HQZDZD",
)

# envia mensagem
wa.send_message(
    to="5571994111866",
    text="oi",
)

print("Mensagem enviada!")

"""
https://graph.facebook.com/v24.0/{{Phone-Number-ID}}/register

{
    "messaging_product": "whatsapp",
    "pin": "123456"
}

curl -i -X POST `
  https://graph.facebook.com/v24.0/954435134428733/messages `
  -H 'Authorization: Bearer EAATYGW2lhwgBQ4NNpLFVOzkhBCfH7SeWuus3RkF47cq9ldlK7QnU9UHhYZAH9xfWlOnf6p3sbbZAZC179mGXxiS6ZBLRt0EU5bWPrkjLOsjP1mAWVrPR8xadDOnEOWDuyhD0SFhojrOpqcKoo68NzqNdtJMGNqdoKEAZCGP1xdD1EMVn6J2CY86XZCWe30HQZDZD' `
  -H 'Content-Type: application/json' `
  -d '{ \"messaging_product\": \"whatsapp\", \"to\":5571994111866 \"\", \"type\": \"template\", \"template\": { \"name\": \"teste\", \"language\": { \"code\": \"pt_BR\" } } }'

"""