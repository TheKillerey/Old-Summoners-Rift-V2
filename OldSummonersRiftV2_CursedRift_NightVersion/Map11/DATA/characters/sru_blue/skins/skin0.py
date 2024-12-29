#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_Blue/SRU_Blue.bin"
    "DATA/Characters/SRU_Blue/Animations/Skin0.bin"
    "DATA/SRU_Blue_Skins_Skin0_Skins_Skin3.bin"
    "DATA/SRU_Blue_Skins_Skin0_Skins_Skin3_Skins_Skin4.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_Blue/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "SRU_Blue"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_Blue/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_Blue/Skins/Base/SRU_Blue.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_Blue/Skins/Base/SRU_Blue.skn"
            texture: string = "ASSETS/Characters/SRU_Blue/Skins/Base/SRU_Blue_Golem_V2.dds"
            skinScale: f32 = 1.18499994
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/SRU_Blue/Skins/Base/SRU_Blue_Bird.dds"
                    submesh: string = "BlueBuff_Bird_Mat"
                }
            }
        }
        armorMaterial: string = "Stone"
        idleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "neutralmonster_buf_blue_defense_big.troy"
                boneName: string = "Root"
            }
        }
        iconCircle: option[string] = {
            "ASSETS/Characters/SRU_Blue/HUD/BlueSentinel_Circle.tex"
        }
        iconCircleScale: option[f32] = {
            1.20000005
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRU_Blue/HUD/BlueSentinel_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            hpPerTick: f32 = 1000
            unitHealthBarStyle: u8 = 5
        }
        mResourceResolver: link = "Characters/SRU_Blue/Skins/Skin0/Resources"
    }
}
