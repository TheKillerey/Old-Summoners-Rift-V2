#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_OrderMinionRanged/SRU_OrderMinionRanged.bin"
    "DATA/Characters/SRU_OrderMinionRanged/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_OrderMinionRanged/Skins/Skin20" = SkinCharacterDataProperties {
        championSkinName: string = "Order_Minion_Ranged_Trueshot_Blue"
        metaDataTags: string = "class:minion"
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Global_Minions_OrderRange_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_OrderRange_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_OrderRange_SFX_events.bnk"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_OrderMinionRanged/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_OrderMinionRanged/Skins/Base/order_minion_caster.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_OrderMinionRanged/Skins/Base/order_minion_caster.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/SRU_OrderMinionRanged/Skins/Base/OrderMinion_caster_TX_CM.dds"
            skinScale: f32 = 0.970000029
            selfIllumination: f32 = 0.699999988
        }
        armorMaterial: string = "Flesh"
        mSpawnParticleName: string = "sru_minionSpawn_01.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/SRU_OrderMinionRanged/HUD/BlueRange_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRU_OrderMinionRanged/HUD/BlueRange_Square.tex"
        }
    }
}
