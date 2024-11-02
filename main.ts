namespace SpriteKind {
    export const bow = SpriteKind.create()
    export const crown = SpriteKind.create()
    export const ring = SpriteKind.create()
}

scene.setBackgroundColor(3)
game.splash("Collect all the missing heirlooms before time runs out!")
//  Create a new sprite with the specified image and assign it to the "player" kind
let mySprite = sprites.create(img`
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
`, SpriteKind.Player)
//  Move sprite with controller
controller.moveSprite(mySprite)
//  Set the current tilemap
tiles.setCurrentTilemap(tilemap`level4`)
//  Place the sprite on a specific tile
tiles.placeOnTile(mySprite, tiles.getTileLocation(1, 14))
//  Make the camera follow the sprite
scene.cameraFollowSprite(mySprite)
//  Start a countdown timer of 15 seconds
info.startCountdown(15)
//  Set up an overlap event between the two sprite kinds
sprites.onOverlap(SpriteKind.Player, SpriteKind.bow, function on_overlap(sprite3: Sprite, other_sprite: Sprite) {
    //  Destroy the 'mySprite' sprite
    sprites.destroy(mySprite)
    //  Increase the countdown by 3 seconds
    info.changeCountdownBy(3)
})
for (let value3 of tiles.getTilesByType(assets.tile`myTile2`)) {
    //  Create a sprite of kind "bow" with a specified image
    mySprite = sprites.create(img`
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
    `, SpriteKind.bow)
    //  Place the sprite on the tile
    tiles.placeOnTile(mySprite, value3)
    //  Change the tile to "tile_path3"
    tiles.setTileAt(value3, sprites.castle.tilePath3)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.crown, function on_on_overlap3(sprite4: Sprite, otherSprite2: Sprite) {
    sprites.destroy(otherSprite2)
    info.changeCountdownBy(3)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile3`, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    
    for (let value of tiles.getTilesByType(assets.tile`
        myTile3
    `)) {
        mySprite = sprites.create(img`
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
        `, SpriteKind.crown)
        tiles.placeOnTile(mySprite, value)
        tiles.setTileAt(value, sprites.castle.tilePath9)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.ring, function on_on_overlap2(sprite5: Sprite, otherSprite3: Sprite) {
    sprites.destroy(mySprite)
    info.changeCountdownBy(3)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function on_overlap_tile3(sprite22: Sprite, location22: tiles.Location) {
    
    for (let value2 of tiles.getTilesByType(assets.tile`
        myTile0
    `)) {
        mySprite = sprites.create(img`
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
        `, SpriteKind.ring)
        tiles.placeOnTile(mySprite, value2)
        tiles.setTileAt(value2, sprites.castle.tilePath7)
    }
})
//  Trigger event when player overlaps with "stair_east"
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairEast, function on_overlap_tile2(sprite2: Sprite, location2: tiles.Location) {
    //  End the game with a win
    game.gameOver(true)
    //  Set the game over effect to confetti
    game.setGameOverEffect(true, effects.confetti)
    //  Play the game over music
    game.setGameOverPlayable(true, music.melodyPlayable(music.jumpUp), false)
})
