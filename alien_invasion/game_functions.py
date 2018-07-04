import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydowm_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动
        ship.moving_right = True
        # 向左移动
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    # elif event.key == pygame.K_UP:
    #     ship.moving_up = True
    # elif event.key == pygame.K_DOWN:
    #     ship.moving_dowm = True
    elif event.key == pygame.K_q:
        sys.exit()

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    # elif event.key == pygame.K_UP:
    #     ship.moving_up = False
    # elif event.key == pygame.K_DOWN:
    #     ship.moving_dowm = False

def check_events(ai_settings,screen,ship,bullets):
    """响应事件"""
    # 监视事件与响应
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydowm_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydowm_events(event, ai_settings, screen, ship, bullets)

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """更新屏幕图像，切换新屏幕"""
    screen.fill(ai_settings.bg_color)
    #绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #绘制飞船与外星人
    ship.blitme()
    aliens.draw(screen)

    # 绘制屏幕可见
    pygame.display.flip()

def check_bullets_aliens_collisions(ai_settings, screen, ship, aliens,bullets):
    # 检查子弹与外星人的碰撞，接触则删除两者
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def update_bullets(ai_settings, screen, ship,aliens,bullets):
    bullets.update()
    # 删除已消失子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullets_aliens_collisions(ai_settings, screen, ship, aliens, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一个新子弹加入编组
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings,alien_width):
    # 创建一个外星人计算一行可容纳外星人数量
    available_space_x = ai_settings.screen_width - 2 * alien_width
    numbers_aliens_x = int(available_space_x / (2 * alien_width))
    return numbers_aliens_x

def get_number_aliens_rows(ai_settings,ship_height,alien_height):
    """计算可容纳行数"""
    available_space_y = ai_settings.screen_height - (3*alien_height) - ship_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    #创建一个外星人加入编组
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_number * alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    """创建一群外星人"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    numbers_aliens_x = get_number_aliens_x(ai_settings,alien_width)
    number_rows = get_number_aliens_rows(ai_settings,ship.rect.height,alien.rect.height)

    #创建一群外星人
    for number_row in range(number_rows):
        for alien_number in range(numbers_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, number_row)

def check_fleet_edges(ai_settings,aliens):
    """当外星人到达边缘时采取措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            changhe_fleet_direction(ai_settings, aliens)
            break

def changhe_fleet_direction(ai_settings,aliens):
    """将外星人群向下移动，并改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    """响应外星人触碰飞船"""
    if stats.ship_left > 0:
        stats.ship_left -= 1
        #清空子弹与外星人
        bullets.empty()
        aliens.empty()
        #创建一群新的外星人，将飞船重置
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """更新外星人位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollide(ship,aliens,bool):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查外星人是否到达底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


