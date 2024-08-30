#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_ChaosMinionSuper/SRU_ChaosMinionSuper.bin"
    "DATA/Characters/SRU_ChaosMinionSuper/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_ChaosMinionSuper/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "Chaos_Minion_Super"
        metaDataTags: string = "class:minion"
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Global_Minions_ChaosSuper_SFX_audio"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_ChaosSuper_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_ChaosSuper_SFX_events.bnk"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_ChaosMinionSuper/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_ChaosMinionSuper/Skins/base/Red_Minion_Superminion.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_ChaosMinionSuper/Skins/base/Red_Minion_Superminion.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/SRU_ChaosMinionSuper/Skins/base/red_superminion_TX_CM.dds"
            skinScale: f32 = 1.14999998
            selfIllumination: f32 = 0.600000024
        }
        armorMaterial: string = "Metal"
        mSpawnParticleName: string = "sru_minionSpawn_Red_01.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/SRU_ChaosMinionSuper/HUD/Redmechmelee_Circle.dds"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRU_ChaosMinionSuper/HUD/Redmechmelee_Square.dds"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 1
        }
    }
}
