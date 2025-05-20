#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_ChaosMinionMelee/SRU_ChaosMinionMelee.bin"
    "DATA/Characters/SRU_ChaosMinionMelee/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_ChaosMinionMelee/Skins/Skin24" = SkinCharacterDataProperties {
        championSkinName: string = "Chaos_Minion_Melee_Bloom_Red"
        metaDataTags: string = "class:minion"
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Global_Minions_ChaosMelee_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_ChaosMelee_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_ChaosMelee_SFX_events.bnk"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_ChaosMinionMelee/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_ChaosMinionMelee/Skins/Base/Chaos_Minion_Melee.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_ChaosMinionMelee/Skins/Base/Chaos_Minion_Melee.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/SRU_ChaosMinionMelee/Skins/Base/ChaosMinion_Melee_TX_CM.dds"
            skinScale: f32 = 0.939999998
            selfIllumination: f32 = 0.600000024
        }
        armorMaterial: string = "Flesh"
        mSpawnParticleName: string = "sru_minionSpawn_Red_01.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/SRU_ChaosMinionMelee/HUD/RedMelee_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRU_ChaosMinionMelee/HUD/RedMelee_Square.tex"
        }
    }
}
