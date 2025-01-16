#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_OrderMinionMelee/SRU_OrderMinionMelee.bin"
    "DATA/Characters/SRU_OrderMinionMelee/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_OrderMinionMelee/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "Order_Minion_Melee"
        metaDataTags: string = "class:minion"
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Global_Minions_OrderMelee_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_OrderMelee_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_OrderMelee_SFX_events.bnk"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_OrderMinionMelee/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_OrderMinionMelee/Skins/Base/Order_Minion_Melee.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_OrderMinionMelee/Skins/Base/Order_Minion_Melee.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/SRU_OrderMinionMelee/Skins/Base/OrderMinion_Melee_TX_CM.dds"
            skinScale: f32 = 0.939999998
            selfIllumination: f32 = 0.600000024
        }
        armorMaterial: string = "Flesh"
        mSpawnParticleName: string = "sru_minionSpawn_01.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/SRU_OrderMinionMelee/HUD/BlueMelee_Circle.dds"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRU_OrderMinionMelee/HUD/BlueMelee_Square.dds"
        }
    }
}
