from services.consulta_service import ConsultaService

service = ConsultaService(None, None, None)

try:
    resultado = service.validar_valor(-150)
    print("Resultado: ", resultado)

except ValueError as erro:
    print("Erro encontrado:", erro)