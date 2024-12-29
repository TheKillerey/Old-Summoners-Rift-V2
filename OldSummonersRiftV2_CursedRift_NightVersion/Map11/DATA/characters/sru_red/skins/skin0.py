#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/SRU_Red_Skins_Skin0_Skins_Skin2.bin"
    "DATA/Characters/SRU_Red/SRU_Red.bin"
    "DATA/Characters/SRU_Red/Animations/Skin0.bin"
    "DATA/SRU_Red_Skins_Skin0_Skins_Skin2_Skins_Skin3.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_Red/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "SRU_Red"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_Red/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_Red/skins/base/SRU_Red.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_Red/skins/base/SRU_Red.skn"
            texture: string = "ASSETS/Characters/SRU_Red/skins/base/SRU_Red.dds"
            skinScale: f32 = 1.47500002
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        armorMaterial: string = "Wood"
        idleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "neutralmonster_buf_red_offense_big.troy"
                boneName: string = "Root"
            }
        }
        iconCircle: option[string] = {
            "ASSETS/Characters/SRU_Red/HUD/Brambleback_Circle.tex"
        }
        iconCircleScale: option[f32] = {
            1.20000005
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRU_Red/HUD/Brambleback_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            hpPerTick: f32 = 1000
            unitHealthBarStyle: u8 = 5
        }
        mResourceResolver: link = "Characters/SRU_Red/Skins/Skin0/Resources"
    }
}
