#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/TurretRubble/TurretRubble.bin"
    "DATA/Characters/TurretRubble/Animations/Skin0.bin"
    "DATA/TurretRubble_Skins_Skin1_Skins_Skin3_Skins_Skin5.bin"
}
entries: map[hash,embed] = {
    "Characters/TurretRubble/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "TurretRubble_SR_Order"
        emoteLoadout: hash = 0x9029a33d
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/TurretRubble/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/TurretRubble/Skins/Base/TurretRubble.skl"
            simpleSkin: string = "ASSETS/Characters/TurretRubble/Skins/Base/TurretRubble.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/TurretRubble/Skins/Base/TurretRubble_TX_CM.dds"
            skinScale: f32 = 0.870000005
            selfIllumination: f32 = 0.5
            brushAlphaOverride: f32 = 1
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        armorMaterial: string = "Flesh"
        idleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "TurretRubble_Idle"
                boneName: string = "root"
            }
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 1
        }
        mResourceResolver: link = 0x7d140ae2
    }
    0x7d140ae2 = ResourceResolver {
        resourceMap: map[hash,link] = {
            "TurretRubble_Idle" = "Characters/TurretRubble/Skins/Skin1/Particles/TurretRubble_Base_Idle"
        }
    }
}