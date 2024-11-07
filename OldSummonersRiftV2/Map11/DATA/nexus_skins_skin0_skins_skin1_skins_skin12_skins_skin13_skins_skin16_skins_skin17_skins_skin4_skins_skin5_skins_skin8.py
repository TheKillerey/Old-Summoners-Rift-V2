#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Nexus/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Order_Nexus" = "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus"
            "Order_Nexus_Crystal_Glow" = "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus_Crystal_Glow"
            "Order_Nexus_Crystal_Glow_on" = "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus_Crystal_Glow_on"
            "Order_Nexus_Base_Glow" = "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus_Base_Glow"
            "Order_Nexus_Base_Glow_on" = "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus_Base_Glow_on"
            "Chaos_Nexus" = "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus"
            "Chaos_Nexus_Crystal_Glow" = "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus_Crystal_Glow"
            "Chaos_Nexus_Crystal_Glow_on" = "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus_Crystal_Glow_on"
            "Chaos_Nexus_Base_Glow" = "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus_Base_Glow"
            "Chaos_Nexus_Base_Glow_on" = "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus_Base_Glow_on"
        }
    }
    "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 89
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "gem_inside"
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -18.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            0.800000012
                            0.899999976
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, -18.5, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 320, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 1 }
                            { 0.800000012, 0, 1, 1 }
                            { 0.699999988, 0, 1, 1 }
                            { 0.600000024, 0, 1, 1 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            0.699999988
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0.300000012, 0 }
                            { 0, 1, 0 }
                            { 0, 1.20000005, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 8, 12 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem_inside_mono.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 89
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "gem_sparkle"
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -18.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            0.800000012
                            0.899999976
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, -18.5, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 320, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem_Sparkle.scb"
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 100
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            0.699999988
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0.300000012, 0 }
                            { 0, 1, 0 }
                            { 0, 1.20000005, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 8, 12 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem_Sparkle.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0.300000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    90
                }
                emitterLinger: option[f32] = {
                    90
                }
                emitterName: string = "littleray"
                importance: u8 = 2
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -50, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        0.100000001
                                        0.899999976
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -5
                                        -1
                                        1
                                        5
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, -50, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.313725501 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.800000012, 0, 1, 0 }
                            { 1, 0.5, 1, 1 }
                            { 1, 0.5, 1, 1 }
                            { 0.800000012, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                isLocalOrientation: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 250, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.500010014
                                    1
                                }
                                keyValues: list[f32] = {
                                    -2
                                    -1
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.670000017
                            1
                        }
                        values: list[vec3] = {
                            { 40, 250, 0 }
                            { 40, 250, 0 }
                            { 40, 100, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.100000001, 0 }
                            { 1.5, 1.5, 0 }
                            { 1, 0.100000001, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/nexus_ray.dds"
                texDiv: vec2 = { 2, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 89
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "gem"
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -18.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            0.800000012
                            0.899999976
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, -18.5, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 320, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 0.5, 1, 0.400000006 }
                            { 1, 0.300000012, 1, 0.400000006 }
                        }
                    }
                }
                doesCastShadow: bool = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            0.699999988
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0.300000012, 0 }
                            { 0, 1, 0 }
                            { 0, 1.20000005, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12.1000004, 8.10000038, 12.1000004 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem_mono.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            0.600000024
                            0.699999988
                            1
                        }
                        values: list[f32] = {
                            10
                            30
                            0
                            0
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.200000003
                                    0.900000036
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.5
                                    2
                                    3
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.200000003
                        }
                    }
                }
                lifetime: option[f32] = {
                    90
                }
                emitterLinger: option[f32] = {
                    90
                }
                emitterName: string = "lightning"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 320, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveRay {}
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.550000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 0, 1, 0 }
                            { 1, 0, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.5, 0.300000012, 1, 1 }
                            { 1, 0.300000012, 1, 1 }
                            { 0.5, 0, 1, 1 }
                        }
                    }
                }
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
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
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 110, 110, 0 }
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
                        }
                        times: list[f32] = {
                            0
                            0.5
                            0.600000024
                            0.629999995
                            1
                        }
                        values: list[vec3] = {
                            { 88, 88, 0 }
                            { 110, 110, 0 }
                            { 110, 110, 0 }
                            { 55, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 1, 0 }
                            { 1.20000005, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/multilightning3.dds"
                numFrames: u16 = 9
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 89
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "gem_streaks"
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -18.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            0.800000012
                            0.899999976
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, -18.5, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 340, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem_Streak.sco"
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.5 }
                            { 1, 1, 1, 0.100000001 }
                            { 1, 0.5, 1, 1 }
                            { 0.5, 0, 0.5, 0 }
                        }
                    }
                }
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            0.699999988
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0.300000012, 0 }
                            { 0, 1, 0 }
                            { 0, 1.20000005, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 8, 12 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/gemstreaks.dds"
                texDiv: vec2 = { 1, 4 }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0.100000001 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 88.1999969
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {
                    4
                }
                lifetime: option[f32] = {
                    91
                }
                isSingleParticle: flag = true
                emitterName: string = "gemon"
                importance: u8 = 2
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 120, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem_Wipe.sco"
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.449999988
                            0.550000012
                            0.800000012
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.200000003 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5000
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 65, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12.1000004, 8.10000038, 12.1000004 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Chaos_Nexus_Wipe.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.300000012 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.899999976 }
                }
            }
        }
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                lifetime: option[f32] = {
                    90
                }
                emitterName: string = "hot"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 120, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraQuad {}
                particleColorTexture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/color-chaosshop.dds"
                meshRenderFlags: u8 = 0
                colorLookUpScales: vec2 = { 1, 0.400000006 }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/RyzeBasicAttack.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 2, 3 }
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 20
                        dynamics: pointer = VfxAnimatedFloatVariableData {
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
                            }
                            times: list[f32] = {
                                0
                                0.5
                                0.600000024
                                1
                            }
                            values: list[f32] = {
                                20
                                40
                                0
                                0
                            }
                        }
                    }
                    scale: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                4
                            }
                        }
                    }
                    birthRotation: embed = ValueFloat {
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
                    birthRotationalVelocity: embed = ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        0.5
                                        0.5
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -10
                                        -10
                                        10
                                        10
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
            }
        }
        particleName: string = "Chaos_Nexus"
        particlePath: string = "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus"
        flags: u16 = 229
    }
    "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus_Crystal_Glow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.600000024
                            1
                        }
                        values: list[f32] = {
                            0
                            0
                            40
                            40
                        }
                    }
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
                lifetime: option[f32] = {
                    90
                }
                emitterName: string = "littleray"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 12, -10 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.541176498, 0, 0.741176486, 0.392156899 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
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
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 60, 60 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/ball03.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    100
                }
                emitterName: string = "glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveCameraQuad {}
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.579999983
                            0.589999974
                            0.639999986
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0, 1, 0 }
                            { 1, 0, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0, 1, 0.600000024 }
                            { 1, 0, 1, 0.600000024 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 0 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/glows.dds"
                startFrame: u16 = 3
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "Chaos_Nexus_Crystal_Glow"
        particlePath: string = "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus_Crystal_Glow"
        flags: u8 = 133
    }
    "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus_Crystal_Glow_on" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
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
                lifetime: option[f32] = {
                    1000000
                }
                emitterName: string = "littleray"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 12, -10 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.541176498, 0, 0.741176486, 0.392156899 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
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
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 60, 60 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/ball03.dds"
            }
        }
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "glow"
                primitive: pointer = VfxPrimitiveCameraQuad {}
                particleColorTexture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/color-turretcrystal.dds"
                meshRenderFlags: u8 = 0
                colorLookUpScales: vec2 = { 1, 0.200000003 }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/glows.dds"
                startFrame: u16 = 3
                texDiv: vec2 = { 2, 2 }
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 50
                    }
                    particleBind: vec2 = { 1, 1 }
                }
            }
        }
        particleName: string = "Chaos_Nexus_Crystal_Glow_on"
        particlePath: string = "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus_Crystal_Glow_on"
        flags: u8 = 132
    }
    "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus_Base_Glow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                lifetime: option[f32] = {
                    90
                }
                emitterName: string = "crown"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 35, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Saucer6.scb"
                    }
                }
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.899999976
                            0.910000026
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0, 1, 0 }
                            { 1, 0, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.5, 0.5, 1, 0.5 }
                            { 0.540000021, 0, 0.74000001, 0.5 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 0.100000001, 0.300000012, 1, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
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
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -10
                                    10
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/cylinder06.dds"
            }
        }
        particleName: string = "Chaos_Nexus_Base_Glow"
        particlePath: string = "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus_Base_Glow"
        flags: u8 = 133
    }
    "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus_Base_Glow_on" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "crown"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 35, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Saucer6.scb"
                    }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.541176498, 0, 0.741176486, 0.392156899 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.300000012 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
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
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -10
                                    10
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/cylinder06.dds"
            }
        }
        particleName: string = "Chaos_Nexus_Base_Glow_on"
        particlePath: string = "Characters/Nexus/Skins/Skin0/Particles/Chaos_Nexus_Base_Glow_on"
        flags: u8 = 133
    }
    "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "gem_inside"
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -18.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            0.800000012
                            0.899999976
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, -18.5, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 320, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 1 }
                            { 0, 0.800000012, 1, 1 }
                            { 0, 0.800000012, 1, 1 }
                            { 0, 0.800000012, 1, 1 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            0.699999988
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0.300000012, 0 }
                            { 0, 1, 0 }
                            { 0, 1.20000005, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 8, 12 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem_inside_mono.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "gem_sparkle"
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -18.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            0.800000012
                            0.899999976
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, -18.5, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 320, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem_Sparkle.scb"
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 100
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            0.699999988
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0.300000012, 0 }
                            { 0, 1, 0 }
                            { 0, 1.20000005, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 8, 12 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem_Sparkle.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0.300000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "littleray"
                importance: u8 = 2
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -50, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        0.100000001
                                        0.899999976
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -5
                                        -1
                                        1
                                        5
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, -50, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.313725501 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.5, 1, 0 }
                            { 0.5, 1, 1, 1 }
                            { 0.5, 1, 1, 1 }
                            { 0, 0.5, 1, 0 }
                        }
                    }
                }
                pass: i16 = 450
                isLocalOrientation: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 250, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.500010014
                                    1
                                }
                                keyValues: list[f32] = {
                                    -2
                                    -1
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.670000017
                            1
                        }
                        values: list[vec3] = {
                            { 40, 250, 0 }
                            { 40, 250, 0 }
                            { 40, 100, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.100000001, 0 }
                            { 1.5, 1.5, 0 }
                            { 1, 0.100000001, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/nexus_ray.dds"
                texDiv: vec2 = { 2, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "gem"
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -18.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            0.800000012
                            0.899999976
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, -18.5, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 320, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0.800000012, 1, 0.400000006 }
                            { 0, 0.800000012, 1, 0.400000006 }
                        }
                    }
                }
                doesCastShadow: bool = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            0.699999988
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0.300000012, 0 }
                            { 0, 1, 0 }
                            { 0, 1.20000005, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12.1000004, 8.10000038, 12.1000004 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem_mono.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            0.600000024
                            0.699999988
                            1
                        }
                        values: list[f32] = {
                            10
                            30
                            0
                            0
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.200000003
                                    0.900000036
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.5
                                    2
                                    3
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.200000003
                        }
                    }
                }
                lifetime: option[f32] = {
                    1
                }
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "lightning"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 320, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveRay {}
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.550000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.5, 0.5, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0.300000012, 1, 0 }
                            { 0, 0.300000012, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 1, 1 }
                            { 0.300000012, 0.600000024, 1, 1 }
                            { 0, 0, 1, 1 }
                        }
                    }
                }
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
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
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 110, 110, 0 }
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
                        }
                        times: list[f32] = {
                            0
                            0.5
                            0.600000024
                            0.629999995
                            1
                        }
                        values: list[vec3] = {
                            { 88, 88, 0 }
                            { 110, 110, 0 }
                            { 110, 110, 0 }
                            { 55, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 1, 0 }
                            { 1.20000005, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/multilightning3.dds"
                numFrames: u16 = 9
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "gem_streaks"
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -18.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            0.800000012
                            0.899999976
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, -18.5, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 340, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem_Streak.sco"
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.5 }
                            { 1, 1, 1, 0.100000001 }
                            { 0.5, 1, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            0.699999988
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0.300000012, 0 }
                            { 0, 1, 0 }
                            { 0, 1.20000005, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 8, 12 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/gemstreaks.dds"
                texDiv: vec2 = { 1, 4 }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0.100000001 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 88.1999969
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {
                    4
                }
                lifetime: option[f32] = {
                    1.5
                }
                isSingleParticle: flag = true
                emitterName: string = "gemon"
                importance: u8 = 2
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 120, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Nexus_Gem_Wipe.sco"
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.449999988
                            0.550000012
                            0.800000012
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.200000003 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5000
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 65, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12.1000004, 8.10000038, 12.1000004 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Order_Nexus_Wipe.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.300000012 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.899999976 }
                }
            }
        }
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "hot"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 120, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraQuad {}
                particleColorTexture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/color-chaosshop.dds"
                meshRenderFlags: u8 = 0
                colorLookUpScales: vec2 = { 1, 0.200000003 }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/RyzeBasicAttack.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 2, 3 }
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 20
                        dynamics: pointer = VfxAnimatedFloatVariableData {
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
                            }
                            times: list[f32] = {
                                0
                                0.5
                                0.600000024
                                1
                            }
                            values: list[f32] = {
                                20
                                40
                                0
                                0
                            }
                        }
                    }
                    scale: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                4
                            }
                        }
                    }
                    birthRotation: embed = ValueFloat {
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
                    birthRotationalVelocity: embed = ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        0.5
                                        0.5
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -10
                                        -10
                                        10
                                        10
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
            }
        }
        particleName: string = "Order_Nexus"
        particlePath: string = "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus"
        flags: u16 = 229
    }
    "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus_Crystal_Glow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.600000024
                            1
                        }
                        values: list[f32] = {
                            0
                            0
                            40
                            40
                        }
                    }
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
                lifetime: option[f32] = {
                    90
                }
                emitterName: string = "littleray"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, -5 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.470588267, 1, 0.392156899 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
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
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 60, 60 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/ball03.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveCameraQuad {}
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.579999983
                            0.589999974
                            0.639999986
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 1, 0 }
                            { 0, 0, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0, 0.5, 1, 0.600000024 }
                            { 0, 0.300000012, 1, 0.600000024 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/glows.dds"
                startFrame: u16 = 3
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "Order_Nexus_Crystal_Glow"
        particlePath: string = "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus_Crystal_Glow"
        flags: u8 = 133
    }
    "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus_Crystal_Glow_on" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                emitterName: string = "littleray"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, -5 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.392156899 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 1, 0 }
                            { 0, 0.5, 1, 1 }
                            { 0.400000006, 1, 1, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
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
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 60, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/ball03.dds"
            }
        }
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "glow"
                primitive: pointer = VfxPrimitiveCameraQuad {}
                particleColorTexture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/color-nexus-gem-glow.dds"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/glows.dds"
                startFrame: u16 = 3
                texDiv: vec2 = { 2, 2 }
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 100
                    }
                    particleBind: vec2 = { 1, 1 }
                }
            }
        }
        particleName: string = "Order_Nexus_Crystal_Glow_on"
        particlePath: string = "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus_Crystal_Glow_on"
        flags: u8 = 132
    }
    "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus_Base_Glow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    90
                }
                emitterName: string = "crown"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 35, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Saucer6.scb"
                    }
                }
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.899999976
                            0.910000026
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 1, 0 }
                            { 0, 0, 1, 0 }
                            { 1, 1, 1, 0.5 }
                            { 0, 0.5, 1, 0.300000012 }
                            { 0, 0.300000012, 1, 0.300000012 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 0.100000001, 0.300000012, 1, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
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
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -10
                                    10
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/cylinder06.dds"
            }
        }
        particleName: string = "Order_Nexus_Base_Glow"
        particlePath: string = "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus_Base_Glow"
        flags: u8 = 133
    }
    "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus_Base_Glow_on" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "crown"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 35, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/Saucer6.scb"
                    }
                }
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.100000001, 0.300000012, 1, 0 }
                            { 0.100000001, 0.300000012, 1, 0.300000012 }
                            { 0.100000001, 0.300000012, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 0.100000001, 0.300000012, 1, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
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
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -10
                                    10
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                texture: string = "ASSETS/Characters/Nexus/Skins/Base/Particles/cylinder06.dds"
            }
        }
        particleName: string = "Order_Nexus_Base_Glow_on"
        particlePath: string = "Characters/Nexus/Skins/Skin0/Particles/Order_Nexus_Base_Glow_on"
        flags: u8 = 132
    }
}
