#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/sru_dragon_water/Animations/Skin0.bin"
    "DATA/Characters/sru_dragon_water/sru_dragon_water.bin"
}
entries: map[hash,embed] = {
    "Characters/sru_dragon_water/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "SRU_Dragon_Water"
        metaDataTags: string = "monstertype:dragon"
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "SRU_Dragon_Ocean"
            }
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Map11_Dragons_Ocean_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Dragons_Ocean_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Dragons_Ocean_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_SRU_Dragon_Ocean_Attack_hit"
                        "Play_sfx_SRU_Dragon_Ocean_Attack_OnCast"
                        "Play_sfx_SRU_Dragon_Ocean_Attack_OnMissileLaunch"
                        "Play_vo_SRU_Dragon_Ocean_Attack_OnCast"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/sru_dragon_water/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/sru_dragon_water/Skins/Base/SRU_Dragon_Water.skl"
            simpleSkin: string = "ASSETS/Characters/sru_dragon_water/Skins/Base/SRU_Dragon_Water.skn"
            texture: string = "ASSETS/Characters/sru_dragon_water/Skins/Base/SRU_Dragon_Water_TX_CM.dds"
            emissiveTexture: string = "ASSETS/Characters/sru_dragon_water/Skins/Base/SRU_Dragon_Water_TX_GM.dds"
            skinScale: f32 = 3
            selfIllumination: f32 = 0.699999988
            brushAlphaOverride: f32 = 1
            reflectionMap: string = "ASSETS/Characters/sru_dragon_water/Skins/Base/SRU_Dragon_Water_CubeMap.dds"
            reflectionOpacityDirect: f32 = 1
            reflectionFresnel: f32 = 0.330000013
            reflectionFresnelColor: rgba = { 127, 255, 255, 255 }
        }
        armorMaterial: string = "Flesh"
        iconCircle: option[string] = {
            "ASSETS/Characters/sru_dragon_water/HUD/Dragon_Circle_Water.dds"
        }
        iconCircleScale: option[f32] = {
            1.20000005
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/sru_dragon_water/HUD/Dragon_Square_Water.dds"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            hpPerTick: f32 = 1000
            attachToBone: string = "Buffbone_Cstm_Healthbar"
            unitHealthBarStyle: u8 = 5
        }
        mResourceResolver: link = "Characters/sru_dragon_water/Skins/Skin0/Resources"
    }
    "Characters/sru_dragon_water/Skins/Skin0/Resources" = ResourceResolver {}
}
