#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_Blue/SRU_Blue.bin"
    "DATA/Characters/SRU_Blue/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_Blue/Skins/Skin1" = SkinCharacterDataProperties {
        championSkinName: string = "SRU_Blue"
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Map11_Blue_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Blue_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Blue_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_SRU_Blue_a2n_buffactivate"
                        "Play_sfx_SRU_Blue_aggro1"
                        "Play_sfx_SRU_Blue_aggro2"
                        "Play_sfx_SRU_Blue_aggro3"
                        "Play_sfx_SRU_Blue_death_cast"
                        "Play_sfx_SRU_Blue_n2a_buffactivate"
                        "Play_sfx_SRU_Blue_spawn_cast"
                        "Play_sfx_SRU_Blue_SRU_BlueBasicAttack2_OnCast"
                        "Play_sfx_SRU_Blue_SRU_BlueBasicAttack2_OnHit"
                        "Play_sfx_SRU_Blue_SRU_BlueBasicAttack3_OnCast"
                        "Play_sfx_SRU_Blue_SRU_BlueBasicAttack3_OnHit"
                        "Play_sfx_SRU_Blue_SRU_BlueBasicAttack_OnCast"
                        "Play_sfx_SRU_Blue_SRU_BlueBasicAttack_OnHit"
                        "Play_sfx_SRU_BlueBasicAttack2_OnCast_OLD"
                        "Play_sfx_SRU_BlueBasicAttack2_OnHit_OLD"
                        "Play_sfx_SRU_BlueBasicAttack3_OnCast_OLD"
                        "Play_sfx_SRU_BlueBasicAttack3_OnHit_OLD"
                        "Play_sfx_SRU_BlueBasicAttack_OnCast_OLD"
                        "Play_sfx_SRU_BlueBasicAttack_OnHit_OLD"
                        "Stop_sfx_SRU_Blue_a2n_buffactivate"
                        "Stop_sfx_SRU_Blue_aggro1"
                        "Stop_sfx_SRU_Blue_aggro2"
                        "Stop_sfx_SRU_Blue_aggro3"
                        "Stop_sfx_SRU_Blue_death_cast"
                        "Stop_sfx_SRU_Blue_n2a_buffactivate"
                        "Stop_sfx_SRU_Blue_spawn_cast"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_Blue/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_Blue/Skins/Base/SRU_Blue.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_Blue/Skins/Base/SRU_Blue.skn"
            texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin01/SRU_Blue_Golem_BM.dds"
            skinScale: f32 = 1.37
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
                boneName: string = "Buffbone_Cstm_BlueBuff"
            }
        }
        iconCircle: option[string] = {
            "ASSETS/Characters/SRU_Blue/HUD/BlueSentinel_Circle.dds"
        }
        iconCircleScale: option[f32] = {
            1.20000005
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRU_Blue/HUD/BlueSentinel_Square.dds"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            hpPerTick: f32 = 1000
            unitHealthBarStyle: u8 = 5
        }
    }
}
