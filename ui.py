import pygame

def draw_menu(screen, menu_font, small_font, width, scaling, menu_buttons):
    screen.fill((220, 220, 220))
    title = menu_font.render("Minesweeper", True, (0, 0, 0))
    screen.blit(title, (width * scaling // 2 - title.get_width() // 2, 40))
    for btn in menu_buttons:
        pygame.draw.rect(screen, (180, 180, 180), btn["rect"])
        label = small_font.render(btn["label"], True, (0, 0, 0))
        label_rect = label.get_rect(center=btn["rect"].center)
        screen.blit(label, label_rect)

def draw_background_selection(screen, menu_font, small_font, width, scaling, bg_buttons):
    screen.fill((200, 200, 255))
    title = menu_font.render("Select Background", True, (0, 0, 0))
    screen.blit(title, (width * scaling // 2 - title.get_width() // 2, 40))
    for btn in bg_buttons:
        pygame.draw.rect(screen, (180, 180, 180), btn["rect"])
        label = small_font.render(btn["label"], True, (0, 0, 0))
        label_rect = label.get_rect(center=btn["rect"].center)
        screen.blit(label, label_rect)
    back_rect = pygame.Rect(width * scaling // 2 - 100, scaling * width - 60, 200, 40)
    pygame.draw.rect(screen, (180, 180, 180), back_rect)
    back_label = small_font.render("Back", True, (0, 0, 0))
    back_label_rect = back_label.get_rect(center=back_rect.center)
    screen.blit(back_label, back_label_rect)

def draw_leaderboard(screen, menu_font, small_font, width, scaling, entries):
    screen.fill((240, 240, 240))
    title = menu_font.render("Leaderboard", True, (0, 0, 0))
    screen.blit(title, (width * scaling // 2 - title.get_width() // 2, 40))
    for i, (name, seconds) in enumerate(entries):
        entry_text = f"{i+1}. {name} - {seconds:.2f}s"
        entry = small_font.render(entry_text, True, (0, 0, 0))
        screen.blit(entry, (width * scaling // 2 - 120, 120 + i * 40))
    info = small_font.render("Click anywhere to return", True, (100, 100, 100))
    screen.blit(info, (width * scaling // 2 - 120, scaling * width - 60))

def draw_name_entry(screen, menu_font, small_font, width, scaling, player_name, win_time):
    screen.fill((220, 255, 220))
    prompt = menu_font.render("Enter your name:", True, (0, 0, 0))
    screen.blit(prompt, (width * scaling // 2 - prompt.get_width() // 2, 120))
    name_box = pygame.Rect(width * scaling // 2 - 100, 200, 200, 50)
    pygame.draw.rect(screen, (255, 255, 255), name_box)
    name_text = menu_font.render(player_name, True, (0, 0, 0))
    screen.blit(name_text, (width * scaling // 2 - name_text.get_width() // 2, 210))
    if win_time is not None:
        time_text = small_font.render(f"Time: {win_time:.2f}s", True, (0, 0, 0))
        screen.blit(time_text, (width * scaling // 2 - 60, 270))
    info = small_font.render("Press Enter to save", True, (100, 100, 100))
    screen.blit(info, (width * scaling // 2 - 100, 320))