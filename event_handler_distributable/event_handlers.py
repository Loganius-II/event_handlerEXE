import pygame

def init_pygame() -> bool:
    try:
        pygame.init()
        pygame.font.init()
        SCREEN = [500,500]
        global screen 
        screen = pygame.display.set_mode(SCREEN)
        global font 
        font = pygame.font.SysFont("Times New Roman", 50 )
        pygame.display.set_caption("Event Handlers", "EH")
        return True
    except:
        return False

def renders(text: str) -> str:
    screen.fill((5,5,5))
    render_font = font.render(text, True, (255,255,255))
    screen.blit(render_font, (100,120))
    pygame.display.flip()

def run_pygame() -> None:
    init = init_pygame()
    if init == True:
        print("[INITIALIZED] Pygame")
    else:
        print("[FAILURE] Could not initialize Pygame")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("[EVENT] EXIT")
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                renders("MOUSEDOWN")
                print("[EVENT] MOUSEDOWN")
            elif event.type == pygame.MOUSEBUTTONUP:
                renders("MOUSEUP")
                print("[EVENT] MOUSEUP")
            elif event.type == pygame.KEYDOWN:

                print("[EVENT] KEYDOWN")
                if event.key == pygame.K_a:
                    renders("KEY A")
                    print("[EVENT] KEY A")
                elif event.key == pygame.K_UP:
                    renders("UP_ARROW")
                    print("[EVENT] UP_ARROW")
                elif event.key == pygame.K_RIGHT:
                    renders("RIGHT_ARROW")
                    print("[EVENT] RIGHT_ARROW")  
                elif event.key == pygame.K_LEFT:
                    renders("LEFT_ARROW")
                    print("[EVENT] LEFT_ARROW")
                elif event.key == pygame.K_DOWN:
                    renders("DOWN_ARROW")
                    print("[EVENT] DOWN_ARROW")    
                else:
                    continue              
def main():
    run_pygame()

if __name__ == '__main__':
    main()

    


