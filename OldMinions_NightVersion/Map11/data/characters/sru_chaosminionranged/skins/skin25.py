#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_ChaosMinionRanged/SRU_ChaosMinionRanged.bin"
    "DATA/Characters/SRU_ChaosMinionRanged/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_ChaosMinionRanged/Skins/Skin25" = SkinCharacterDataProperties {
        championSkinName: string = "Chaos_Minion_Ranged_Bloom_Blue"
        metaDataTags: string = "class:minion"
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Global_Minions_ChaosRange_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_ChaosRange_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_ChaosRange_SFX_events.bnk"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_ChaosMinionRanged/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_ChaosMinionRanged/Skins/Base/Chaos_Minion_Caster.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_ChaosMinionRanged/Skins/Base/Chaos_Minion_Caster.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/SRU_ChaosMinionRanged/Skins/Base/red_caster_TX_CM_Blue.dds"
            skinScale: f32 = 0.870000005
            selfIllumination: f32 = 0.699999988
        }
        armorMaterial: string = "Flesh"
        mSpawnParticleName: string = "sru_minionSpawn_Red_01.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/SRU_ChaosMinionRanged/HUD/BlueRange_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRU_ChaosMinionRanged/HUD/BlueRange_Square.tex"
        }
    }
}
