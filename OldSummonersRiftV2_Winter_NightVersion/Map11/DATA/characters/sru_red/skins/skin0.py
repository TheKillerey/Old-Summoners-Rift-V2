#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_Red/SRU_Red.bin"
    "DATA/Characters/SRU_Red/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_Red/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "SRU_Red"
        emoteLoadout: hash = 0x25d79241
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Map11_Red_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Red_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Red_SFX_events.bnk"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_Red/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_Red/skins/base/SRU_Red.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_Red/skins/base/SRU_Red.skn"
            texture: string = "ASSETS/Characters/SRU_Red/skins/base/SRU_Red.dds"
            skinScale: f32 = 2.07500005
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
            "Brambleback_Circle.tex"
        }
        iconCircleScale: option[f32] = {
            1.20000005
        }
        iconSquare: option[string] = {
            "Brambleback_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            hpPerTick: f32 = 1000
            unitHealthBarStyle: u8 = 5
        }
    }
}
