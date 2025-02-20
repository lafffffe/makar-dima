import requests, pygame, sys, os


server_address = 'https://static-maps.yandex.ru/v1?'
api_key = '84e19037-c050-4c65-b7a7-4fb37ae52f28'
x = 37.530887
y = 55.703118
spn = 0.002

def response(server_address, api_key, x, y, spn):
    map_request = f"{server_address}ll={str(x)},{str(y)}&spn={str(spn)},{str(spn)}&apikey={api_key}"
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
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((600, 450))
response(server_address, api_key, x, y, spn)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                spn += 0.001
                response(server_address, api_key, x, y, spn)
            elif event.key == pygame.K_PAGEDOWN:
                spn -= 0.001
                response(server_address, api_key, x, y, spn)
            elif event.key == pygame.K_UP:
                y += 0.00001
                response(server_address, api_key, x, y, spn)
            elif event.key == pygame.K_DOWN:
                y -= 0.00001
                response(server_address, api_key, x, y, spn)
            elif event.key == pygame.K_RIGHT:
                x += 0.00001
                response(server_address, api_key, x, y, spn)
            elif event.key == pygame.K_LEFT:
                x -= 0.00001
                response(server_address, api_key, x, y, spn)
pygame.quit()
