import pygame
import json

# เริ่มต้น pygame
pygame.init()

# โหลดข้อมูลแผนที่จาก JSON
json_file_path = "Tiny_Swords/map.json"
with open(json_file_path, "r") as f:
    map_data = json.load(f)

# โหลดสไปรท์จาก Spritesheet
spritesheet_path = "Tiny_Swords/spritesheet.png"  # Remove the extra 's' at the start
spritesheet = pygame.image.load(spritesheet_path)

# กำหนดขนาดไทล์จาก JSON
tile_size = map_data["tileSize"]

# สร้างหน้าจอแสดงผล
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tile Map Renderer")

# ฟังก์ชันดึงไทล์จาก Spritesheet
def get_tile(spritesheet, tile_id, tile_size):
    cols = spritesheet.get_width() // tile_size
    row = tile_id // cols
    col = tile_id % cols
    x, y = col * tile_size, row * tile_size
    return spritesheet.subsurface((x, y, tile_size, tile_size))

# วาดแผนที่
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # วาดไทล์จาก JSON
    for layer in map_data["layers"]:
        for tile in layer["tiles"]:
            tile_id = int(tile["id"])
            x, y = tile["x"], tile["y"]
            tile_image = get_tile(spritesheet, tile_id, tile_size)
            screen.blit(tile_image, (x, y))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()