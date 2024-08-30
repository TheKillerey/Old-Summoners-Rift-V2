#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/DestroyedTower/DestroyedTower.bin"
    "DATA/Characters/DestroyedTower/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/DestroyedTower/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "DestroyedTowerBase"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/DestroyedTower/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/DestroyedTower/DestroyedTower.skl"
            simpleSkin: string = "ASSETS/Characters/DestroyedTower/DestroyedTower.skn"
            texture: string = "ASSETS/Characters/DestroyedTower/tower_destroyed_diff.dds"
            skinScale: f32 = 0.870000005
            selfIllumination: f32 = 0.5
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        idleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "DestroyedBuilding_idle.troy"
                boneName: string = "root"
            }
        }
    }
}
