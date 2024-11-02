@namespace
class SpriteKind:
    bow = SpriteKind.create()
    crown = SpriteKind.create()
    ring = SpriteKind.create()

scene.set_background_color(3)
game.splash("Collect all the missing heirlooms before time runs out!")

    # Create a new sprite with the specified image and assign it to the "player" kind
mySprite = sprites.create(img("""
    . . . . . f f 4 4 f f . . . . .
    . . . . f 5 4 5 5 4 5 f . . . .
    . . . f e 4 5 5 5 5 4 e f . . .
    . . f b 3 e 4 4 4 4 e 3 b f . .
    . . f 3 3 3 3 3 3 3 3 3 3 f . .
    . f 3 3 e b 3 e e 3 b e 3 3 f .
    . f 3 3 f f e e e e f f 3 3 f .
    . f b b f b f e e f b f b b f .
    . f b b e 1 f 4 4 f 1 e b b f .
    f f b b f 4 4 4 4 4 4 f b b f f
    f b b f f f e e e e f f f b b f
    . f e e f b d d d d b f e e f .
    . . e 4 c d d d d d d c 4 e . .
    . . e f b d b d b d b b f e . .
    . . . f f 1 d 1 d 1 d f f . . .
    . . . . . f f b b f f . . . . .
"""),
    SpriteKind.player)

# Move sprite with controller
controller.move_sprite(mySprite)

# Set the current tilemap
tiles.set_current_tilemap(tilemap("level4"))

# Place the sprite on a specific tile
tiles.place_on_tile(mySprite, tiles.get_tile_location(1, 14))

# Make the camera follow the sprite
scene.camera_follow_sprite(mySprite)

# Start a countdown timer of 15 seconds
info.start_countdown(15)

def on_overlap(sprite3: Sprite, other_sprite: Sprite):
    # Destroy the 'mySprite' sprite
    sprites.destroy(mySprite)
    
    # Increase the countdown by 3 seconds
    info.change_countdown_by(3)

# Set up an overlap event between the two sprite kinds
sprites.on_overlap(SpriteKind.player, SpriteKind.bow, on_overlap)


for value3 in tiles.get_tiles_by_type(assets.tile("myTile2")):
    # Create a sprite of kind "bow" with a specified image
    mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        3 3 . . . . . . . . 3 3 . . . .
        3 3 3 . . . . . . 3 3 3 . . . .
        3 3 3 3 . . . . 3 3 3 3 . . . .
        3 3 3 3 3 . . 3 3 3 3 3 . . . .
        3 3 3 3 3 1 1 3 3 3 3 3 . . . .
        3 3 3 3 3 1 1 3 3 3 3 3 . . . .
        3 3 3 3 3 . . 3 3 3 3 3 . . . .
        3 3 3 3 . . . . 3 3 3 3 . . . .
        3 3 3 . . . . . . 3 3 3 . . . .
        3 3 . . . . . . . . 3 3 . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """), SpriteKind.bow)
    
    # Place the sprite on the tile
    tiles.place_on_tile(mySprite, value3)
    
    # Change the tile to "tile_path3"
    tiles.set_tile_at(value3, sprites.castle.tile_path3)



def on_on_overlap3(sprite4, otherSprite2):
    sprites.destroy(otherSprite2)
    info.change_countdown_by(3)

sprites.on_overlap(SpriteKind.player, SpriteKind.crown, on_on_overlap3)


def on_overlap_tile(sprite: Sprite, location: tiles.Location):
    global mySprite
    
    for value in tiles.get_tiles_by_type(assets.tile("""
        myTile3
    """)):
        mySprite = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            5 5 . . . . 5 5 . . . . 5 5 . .
            5 5 . 5 5 . 5 5 . 5 5 . 5 5 . .
            5 5 . 5 5 . 5 5 . 5 5 . 5 5 . .
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 . .
            1 5 5 5 1 5 5 5 5 1 5 5 5 1 . .
            5 5 9 5 5 5 3 3 5 5 5 9 5 5 . .
            5 9 8 9 5 3 2 2 3 5 9 8 9 5 . .
            5 5 9 5 5 5 3 3 5 5 5 9 5 5 . .
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 . .
            1 5 5 5 1 5 5 5 5 1 5 5 5 1 . .
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
        """), SpriteKind.crown)
        
        tiles.place_on_tile(mySprite, value)
        tiles.set_tile_at(value, sprites.castle.tile_path9)

scene.on_overlap_tile(SpriteKind.player, assets.tile("myTile3"), on_overlap_tile)


def on_on_overlap2(sprite5: Sprite, otherSprite3: Sprite):
    sprites.destroy(mySprite)
    info.change_countdown_by(3)

sprites.on_overlap(SpriteKind.player, SpriteKind.ring, on_on_overlap2)


def on_overlap_tile3(sprite22: Sprite, location22: tiles.Location):
    global mySprite
    
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile0
    """)):
        mySprite = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . 1 9 9 9 9 . . . . . . .
            . . . 9 9 9 9 9 9 9 . . . . . .
            . . . 9 9 9 9 9 9 9 . . . . . .
            . . . . 9 9 9 9 9 . . . . . . .
            . . . . . 9 9 9 . . . . . . . .
            . . . 5 5 5 5 5 5 5 . . . . . .
            . . 5 . . . . . . . 5 . . . . .
            . 5 . . . . . . . . . 5 . . . .
            . 5 . . . . . . . . . 5 . . . .
            . 5 . . . . . . . . . 5 . . . .
            . 5 . . . . . . . . . 5 . . . .
            . . 5 . . . . . . . 5 . . . . .
            . . . 5 5 5 5 5 5 5 . . . . . .
        """), SpriteKind.ring)
        
        
        tiles.place_on_tile(mySprite, value2)
        tiles.set_tile_at(value2, sprites.castle.tile_path7)

scene.on_overlap_tile(SpriteKind.player, assets.tile("myTile0"), on_overlap_tile3)


def on_overlap_tile2(sprite2: Sprite, location2: tiles.Location):
    # End the game with a win
    game.game_over(True)
    
    # Set the game over effect to confetti
    game.set_game_over_effect(True, effects.confetti)
    
    # Play the game over music
    game.set_game_over_playable(True, music.melody_playable(music.jump_up), False)

# Trigger event when player overlaps with "stair_east"
scene.on_overlap_tile(SpriteKind.player, sprites.dungeon.stair_east, on_overlap_tile2)
