import requests, pygame, sys, os


server_address = 'https://static-maps.yandex.ru/v1?'
api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
ll = '37.530887,55.703118'
spn = 0.002

def response(server_address, api_key, ll, spn):
    map_request = f"{server_address}ll={ll}&spn={str(spn)},{str(spn)}&apikey={api_key}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    os.remove(map_file)


pygame.init()
screen = pygame.display.set_mode((600, 450))
response(server_address, api_key, ll, spn)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.K_PAGEUP:
            spn += 0.01
            response(server_address, api_key, ll, spn)
        elif event.type == pygame.K_PAGEDOWN:
            spn -= 0.01
            response(server_address, api_key, ll, spn)
    pygame.display.flip()
pygame.quit()
