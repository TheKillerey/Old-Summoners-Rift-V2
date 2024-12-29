#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/sru_dragon_fire/sru_dragon_fire.bin"
    "DATA/Characters/sru_dragon_fire/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/sru_dragon_fire/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "SRU_Dragon_Fire"
        metaDataTags: string = "monstertype:dragon"
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "SRU_Dragon_Infernal"
            }
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Map11_Dragons_Infernal_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Dragons_Infernal_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Dragons_Infernal_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_SRU_Dragon_Infernal_Attack_OnCast"
                        "Play_sfx_SRU_Dragon_Infernal_Attack_OnHitLocation"
                        "Play_sfx_SRU_Dragon_Infernal_Attack_OnMissileLaunch"
                        "Play_vo_SRU_Dragon_Infernal_Attack_OnCast"
                    }
                }
                BankUnit {
                    name: string = "NPC_Map11_Dragons_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Dragons_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Dragons_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_SRU_Dragon_ag2al_buffactive"
                        "Play_sfx_SRU_Dragon_aggro1_buffactive"
                        "Play_sfx_SRU_Dragon_aggro3_buffactive"
                        "Play_sfx_SRU_Dragon_aggro4_buffactive"
                        "Play_sfx_SRU_Dragon_aggro5_buffactive"
                        "Play_sfx_SRU_Dragon_aggro6_buffactive"
                        "Play_sfx_SRU_Dragon_aggro7_buffactive"
                        "Play_sfx_SRU_Dragon_al2ag_buffactive"
                        "Play_sfx_SRU_Dragon_al2n_buffactive"
                        "Play_sfx_SRU_Dragon_alert2_buffactive"
                        "Play_sfx_SRU_Dragon_alert3_buffactive"
                        "Play_sfx_SRU_Dragon_death_cast"
                        "Play_sfx_SRU_Dragon_death_reverb"
                        "Play_sfx_SRU_Dragon_DragonFireball2_OnMissileCast"
                        "Play_sfx_SRU_Dragon_DragonFireball2_OnMissileLaunch"
                        "Play_sfx_SRU_Dragon_DragonFireball_hit"
                        "Play_sfx_SRU_Dragon_DragonFireball_OnCast"
                        "Play_sfx_SRU_Dragon_DragonTakeOff_cast"
                        "Play_sfx_SRU_Dragon_hover_buffactive"
                        "Play_sfx_SRU_Dragon_landing_buffactive"
                        "Play_sfx_SRU_Dragon_n2al_buffactive"
                        "Play_sfx_SRU_Dragon_spawn_cast"
                        "Play_sfx_SRU_Dragon_spawn_cast_vox"
                        "Stop_sfx_SRU_Dragon_ag2al_buffactive"
                        "Stop_sfx_SRU_Dragon_aggro1_buffactive"
                        "Stop_sfx_SRU_Dragon_aggro3_buffactive"
                        "Stop_sfx_SRU_Dragon_aggro4_buffactive"
                        "Stop_sfx_SRU_Dragon_aggro5_buffactive"
                        "Stop_sfx_SRU_Dragon_aggro6_buffactive"
                        "Stop_sfx_SRU_Dragon_aggro7_buffactive"
                        "Stop_sfx_SRU_Dragon_al2ag_buffactive"
                        "Stop_sfx_SRU_Dragon_al2n_buffactive"
                        "Stop_sfx_SRU_Dragon_alert2_buffactive"
                        "Stop_sfx_SRU_Dragon_alert3_buffactive"
                        "Stop_sfx_SRU_Dragon_death_cast"
                        "Stop_sfx_SRU_Dragon_death_vox_cast"
                        "Stop_sfx_SRU_Dragon_DragonFireball2_OnMissileCast"
                        "Stop_sfx_SRU_Dragon_DragonFireball2_OnMissileLaunch"
                        "Stop_sfx_SRU_Dragon_DragonFireball_OnCast"
                        "Stop_sfx_SRU_Dragon_hover_buffactive"
                        "Stop_sfx_SRU_Dragon_landing_buffactive"
                        "Stop_sfx_SRU_Dragon_n2al_buffactive"
                        "Stop_sfx_SRU_Dragon_spawn_cast_vox"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/sru_dragon_fire/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/sru_dragon_fire/Skins/Base/SRU_Dragon_Fire.skl"
            simpleSkin: string = "ASSETS/Characters/sru_dragon_fire/Skins/Base/SRU_Dragon_Fire.skn"
            texture: string = "ASSETS/Characters/sru_dragon_fire/Skins/Base/SRU_Dragon_Fire_TX_CM.dds"
            skinScale: f32 = 3
            selfIllumination: f32 = 0.699999988
            brushAlphaOverride: f32 = 1
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        armorMaterial: string = "Flesh"
        iconCircle: option[string] = {
            "ASSETS/Characters/sru_dragon_fire/HUD/Dragon_Circle_Fire.dds"
        }
        iconCircleScale: option[f32] = {
            1.20000005
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/sru_dragon_fire/HUD/Dragon_Square_Fire.dds"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            hpPerTick: f32 = 1000
            attachToBone: string = "Buffbone_Cstm_Healthbar"
            unitHealthBarStyle: u8 = 5
        }
        mResourceResolver: link = "Characters/sru_dragon_fire/Skins/Skin0/Resources"
    }
    "Characters/sru_dragon_fire/Skins/Skin0/Resources" = ResourceResolver {}
}
