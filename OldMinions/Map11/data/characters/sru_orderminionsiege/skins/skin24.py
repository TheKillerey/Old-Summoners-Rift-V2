#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_OrderMinionSiege/SRU_OrderMinionSiege.bin"
    "DATA/Characters/SRU_OrderMinionSiege/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_OrderMinionSiege/Skins/Skin24" = SkinCharacterDataProperties {
        championSkinName: string = "Order_Minion_Siege_Bloom_Blue"
        metaDataTags: string = "class:minion"
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Global_Minions_OrderSiege_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_OrderSiege_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_OrderSiege_SFX_events.bnk"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_OrderMinionSiege/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_OrderMinionSiege/Skins/Base/Order_Minion_Siege.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_OrderMinionSiege/Skins/Base/Order_Minion_Siege.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/SRU_OrderMinionSiege/Skins/Base/Order_Minion_Siege_TX_CM.dds"
            skinScale: f32 = 1.02499998
            selfIllumination: f32 = 0.600000024
        }
        armorMaterial: string = "Stone"
        mSpawnParticleName: string = "sru_minionSpawn_01.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/SRU_OrderMinionSiege/HUD/Bluemechcannon_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRU_OrderMinionSiege/HUD/Bluemechcannon_Square.tex"
        }
    }
}
