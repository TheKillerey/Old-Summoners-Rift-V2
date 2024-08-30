#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_Gromp/SRU_Gromp.bin"
    "DATA/Characters/SRU_Gromp/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_Gromp/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "SRU_Gromp"
        emoteLoadout: hash = 0xd3eee753
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Map11_Gromp_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Gromp_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Gromp_SFX_events.bnk"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_Gromp/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/SRU_Gromp.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/SRU_Gromp.skn"
            texture: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/SRU_Gromp_base_TX_CM.dds"
            glossTexture: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/SRU_Gromp_base_TX_GM.dds"
            skinScale: f32 = 2.29999995
            selfIllumination: f32 = 0.699999988
            reflectionMap: string = "SRU_Gromp_base_CubeMap.dds"
            reflectionOpacityDirect: f32 = 1
            reflectionFresnel: f32 = 0.300000012
            reflectionFresnelColor: rgba = { 77, 77, 77, 255 }
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/SRU_Gromp_mini_TX_CM.dds"
                    submesh: string = "SRU_Gromp_mini_mat"
                }
            }
        }
        armorMaterial: string = "Flesh"
        iconCircle: option[string] = {
            "Gromp_Circle.dds"
        }
        iconSquare: option[string] = {
            "Gromp_Square.dds"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 5
        }
        mResourceResolver: link = "Characters/SRU_Gromp/Skins/Skin0/Resources"
    }
    "Characters/SRU_Gromp/Skins/Skin0/Particles/Gromp_Heal_Pickup" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.699999988
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.6999998
                }
                lifetime: option[f32] = {
                    1
                }
                emitterLinger: option[f32] = {
                    0.200000003
                }
                emitterName: string = "Burst"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 10, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 40, 110, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.5
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 40, 110, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.5, 1, 0.5, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.200000003
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.5, 1, 0.5, 0 }
                            { 0.5, 1, 0.5, 0.75 }
                            { 0.5, 1, 0.5, 0.100000001 }
                            { 0.5, 1, 0.5, 0 }
                        }
                    }
                }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 100, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                        }
                        values: list[vec3] = {
                            { 50, 100, 1 }
                            { 15.000001, 30.0000019, 0.300000012 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 0.310000002, 0.310000002, 0.310000002 }
                            { 0.5, 0.5, 0.5 }
                            { 0.699999988, 1, 1 }
                            { 1, 1.20000005, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/Particles/Global_Lifesteal_Strands_2x2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11.1999998
                }
                lifetime: option[f32] = {
                    1
                }
                emitterLinger: option[f32] = {
                    0.200000003
                }
                emitterName: string = "GlowLoop"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 10, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 50, 0 }
                            }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.5, 1, 0.5, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.5, 1, 0.5, 0 }
                            { 0.5, 1, 0.5, 0.200000003 }
                            { 0.5, 1, 0.5, 0.100000001 }
                            { 0.5, 1, 0.5, 0 }
                        }
                    }
                }
                isDirectionOriented: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 100, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 0.310000002, 0.310000002, 0.310000002 }
                            { 0.5, 0.5, 0.5 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/Particles/bigglow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10.8999996
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "MeshMiddle"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -100, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/Particles/global_lifesteal_mesh.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0963627771
                            0.307043642
                            0.707100332
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.0722222254 }
                            { 1, 1, 1, 0.923456788 }
                            { 1, 1, 1, 0.757901251 }
                            { 1, 1, 1, 0.0111111114 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -70, -180, 0 }
                }
                flexBirthRotationalVelocity0: pointer = FlexValueVector3 {}
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.800000012, 0.800000012, 0.800000012 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 1, 0.349999994 }
                            { 0.75, 0.949999988, 0.600000024 }
                            { 0.649999976, 0.550000012, 1.10000002 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/Particles/Global_Lifesteal_MeshSwipe.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -1, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                emitterLinger: option[f32] = {
                    0.200000003
                }
                emitterName: string = "SparkleLoop"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 5, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 0, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 200, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 10, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 50, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 1.00000012, 0, 0 }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.5, 1, 0.5, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.5, 1, 0.5, 0 }
                            { 0.5, 1, 0.5, 0 }
                            { 0.5, 1, 0.5, 1 }
                            { 0.5, 1, 0.5, 0 }
                        }
                    }
                }
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    90
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 0.310000002, 0.310000002, 0.310000002 }
                            { 0.200000003, 0.200000003, 0.200000003 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/Particles/Global_Item_HealthPotion_4x4_Sparkle.DDS"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1.79999995
                }
                emitterName: string = "trail_"
                importance: u8 = 2
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -10, 0 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                                0.5
                            }
                            values: list[vec3] = {
                                { 50, 0, 0 }
                                { 10, 0, 0 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                    }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0666666701, 0.266666681, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.150000006
                            0.400000006
                            0.699999988
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.300000012
                        }
                        values: list[vec3] = {
                            { 6, 0, 0 }
                            { 15, 0, 0 }
                            { 6, 0, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.00999999978
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 2, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/Particles/Global_Lifesteal_MisTrail.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1.79999995
                }
                emitterName: string = "trail_1"
                importance: u8 = 2
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -50, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                                0.5
                            }
                            values: list[vec3] = {
                                { -50, 0, 0 }
                                { -10, 0, 0 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                    }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0666666701, 0.266666681, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.150000006
                            0.400000006
                            0.699999988
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.300000012
                        }
                        values: list[vec3] = {
                            { 6, 0, 0 }
                            { 45, 0, 0 }
                            { 6, 0, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.00999999978
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.200000003, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/Particles/Global_Lifesteal_MisTrail.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1.79999995
                }
                emitterName: string = "trail_2"
                importance: u8 = 2
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -35, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                                0.5
                            }
                            values: list[vec3] = {
                                { -35, 0, 0 }
                                { -7, 0, 0 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                    }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0666666701, 0.266666681, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.150000006
                            0.400000006
                            0.699999988
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.300000012
                        }
                        values: list[vec3] = {
                            { 6, 0, 0 }
                            { 45, 0, 0 }
                            { 6, 0, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.00999999978
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.200000003, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/Particles/Global_Lifesteal_MisTrail.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                emitterLinger: option[f32] = {
                    0.200000003
                }
                emitterName: string = "SparkleLoop1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 5, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 0, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 200, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 10, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 50, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 1.00000012, 0, 0 }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0588235296, 0.200000003, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.0588235296, 0.200000003, 1, 0 }
                            { 0.0588235296, 0.200000003, 1, 0 }
                            { 0.0588235296, 0.200000003, 1, 1 }
                            { 0.0588235296, 0.200000003, 1, 0 }
                        }
                    }
                }
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    90
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 0.310000002, 0.310000002, 0.310000002 }
                            { 0.200000003, 0.200000003, 0.200000003 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/Particles/Global_Item_HealthPotion_4x4_Sparkle.DDS"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1.79999995
                }
                emitterName: string = "trail_3"
                importance: u8 = 2
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -50, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                                0.5
                            }
                            values: list[vec3] = {
                                { -50, 0, 0 }
                                { -10, 0, 0 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 100, 0, 0 }
                        }
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/Particles/color-aura-green.DDS"
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.150000006
                            0.400000006
                            0.699999988
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.300000012
                        }
                        values: list[vec3] = {
                            { 6, 0, 0 }
                            { 45, 0, 0 }
                            { 6, 0, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.00999999978
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.200000003, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Gromp/Skins/Base/Particles/Global_Lifesteal_MisTrail.dds"
            }
        }
        particleName: string = "Gromp_Heal_Pickup"
        particlePath: string = "Characters/SRU_Gromp/Skins/Skin0/Particles/Gromp_Heal_Pickup"
        soundPersistentDefault: string = "Play_sfx_SRU_Gromp_heal_missilelaunch"
    }
    "Characters/SRU_Gromp/Skins/Skin0/Particles/Gromp_Heal_Impact" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLinger: option[f32] = {
                    10.3000002
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Flash"
                importance: u8 = 2
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.666666687, 1, 0.498039216, 1 }
                            { 0, 1, 0, 1 }
                            { 0, 0.666666687, 0, 0 }
                        }
                    }
                }
                pass: i16 = 20
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 4, 4 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 4, 4 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Gromp_Heal_LensFlare_02desat.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.25
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.075000003
                                    0.200000003
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Sparks"
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.333333343, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.639994025 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.999000013
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.639994025 }
                            { 1, 1, 1, 0.639994025 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    190
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5.5999999, 8.39999962, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 5.5999999, 8.39999962, 40 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 5, 7, 0.200000003 }
                            { 7, 5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Gromp_Heal_DeathSparks_4x4.dds"
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            1
                            0.5
                        }
                    }
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "Sparks_Up"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 15, 15 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 25, 100, 25 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 25, 100, 25 }
                            }
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 1, 0.498039216, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.725993991 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.725993991 }
                            { 1, 1, 1, 0.725993991 }
                            { 1, 1, 1, 0.725993991 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    3
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 60, 0, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Gromp_Heal_Spark.dds"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "manaSparkles"
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 1 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 90, 30 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 30, 90, 30 }
                            }
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.570000768 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.333333343, 1, 1, 0 }
                            { 0, 0.666666687, 1, 1 }
                            { 0, 0.333333343, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    3
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 0, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.150000006
                            0.200000003
                            0.300000012
                            0.400000006
                            0.449999988
                            0.550000012
                            0.649999976
                            0.699999988
                            0.75
                            0.850000024
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.699999988, 1, 1 }
                            { 0.899999976, 1, 1 }
                            { 0.774999976, 1, 1 }
                            { 0.899999976, 1, 1 }
                            { 0.625, 1, 1 }
                            { 0.875, 1, 1 }
                            { 0.474999994, 1, 1 }
                            { 0.75, 1, 1 }
                            { 0.524999976, 1, 1 }
                            { 0.725000024, 0.833333313, 1 }
                            { 0.5, 0.5, 1 }
                            { 0, 0, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Gromp_Heal_Spark.dds"
                uvMode: u8 = 2
            }
        }
        particleName: string = "Gromp_Heal_Impact"
        particlePath: string = "Characters/SRU_Gromp/Skins/Skin0/Particles/Gromp_Heal_Impact"
        soundPersistentDefault: string = "Play_sfx_SRU_Gromp_heal_buffactivate"
        flags: u8 = 228
    }
    "Characters/SRU_Gromp/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0xc4cfe194 = "Characters/SRU_Gromp/Skins/Skin0/Particles/Gromp_Heal_Pickup"
            0xf76b2f0a = "Characters/SRU_Gromp/Skins/Skin0/Particles/Gromp_Heal_Impact"
        }
    }
}
