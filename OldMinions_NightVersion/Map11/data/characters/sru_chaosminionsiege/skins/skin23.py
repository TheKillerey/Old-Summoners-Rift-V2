#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_ChaosMinionSiege/SRU_ChaosMinionSiege.bin"
    "DATA/Characters/SRU_ChaosMinionSiege/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    0xeb22568e = SkinCharacterDataProperties {
        championSkinName: string = "Chaos_Minion_Siege_SRS_Blue"
        metaDataTags: string = "class:minion"
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Global_Minions_ChaosSiege_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_ChaosSiege_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_ChaosSiege_SFX_events.bnk"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_ChaosMinionSiege/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_ChaosMinionSiege/Skins/Base/Chaos_Minion_Siege.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_ChaosMinionSiege/Skins/Base/Chaos_Minion_Siege.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/SRU_ChaosMinionSiege/Skins/Base/Chaos_Minion_Siege_TX_CM_Blue.dds"
            skinScale: f32 = 1.02499998
            selfIllumination: f32 = 0.600000024
        }
        armorMaterial: string = "Metal"
        mSpawnParticleName: string = "sru_minionSpawn_Red_01.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/SRU_ChaosMinionSiege/HUD/Bluemechcannon_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRU_ChaosMinionSiege/HUD/Bluemechcannon_Square.tex"
        }
    }
}
