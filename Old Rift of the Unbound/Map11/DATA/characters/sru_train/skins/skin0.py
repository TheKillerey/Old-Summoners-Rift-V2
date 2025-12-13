#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_Train/SRU_Train.bin"
    "DATA/Characters/SRU_Train/Animations/Skin0.bin"
    "DATA/SRU_Train_Skins_Skin0_Skins_Skin1.bin"
}
entries: map[hash,embed] = {
    0xcc06bb96 = SkinCharacterDataProperties {
        championSkinName: string = "SRU_Train"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = 0xcfb099a3
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_Train/Skins/Base/SRU_Train_Base.Milkshake_Env.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_Train/Skins/Base/SRU_Train_Base.Milkshake_Env.skn"
            texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/SRU_Train_Base_TX_CM.Milkshake_Env.tex"
            selfIllumination: f32 = 0.7
            skinScale: f32 = 0
            overrideBoundingBox: option[vec3] = {
                { 800, 200, 800 }
            }
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/SRU_Train_Base_Poro_TX_CM.Milkshake_Env.tex"
                    submesh: string = "Poro"
                }
            }
        }
        emoteBuffbone: string = ""
        godrayFXbone: string = ""
        healthBarData: embed = CharacterHealthBarDataRecord {
            hpPerTick: f32 = 1
        }
        mResourceResolver: link = 0x643f504c
    }
    "Characters/SRU_Train/Skins/Skin0/Particles/SRU_Train_Base_I_TrainSteam" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.75
                        }
                    }
                }
                emitterName: string = "Steam_Add4"
                importance: u8 = 1
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 550, 0 }
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
                                    0.6
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 550, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    3
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
                        }
                        values: list[vec3] = {
                            { 3, 3, 3 }
                        }
                    }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 5, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    height: f32 = 10
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.48, 0.91, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
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
                        values: list[vec4] = {
                            { 0.48, 0.91, 1, 1 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.2
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.2
                    erosionFeatherOut: f32 = 0.2
                    erosionMapName: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Base_SmokeErode.Milkshake_Env.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 0 }
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
                            { 90, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 60, 1.5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.7
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
                            { 100, 60, 1.5 }
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
                            { 0.1, 0, 0 }
                            { 1.2, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/Base_Mis_AlphaCircleGradient.Milkshake_Env.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Cloud_Pattern.Milkshake_Env.tex"
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
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
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
        }
        particleName: string = "SRU_Train_Base_I_TrainSteam"
        particlePath: string = "Characters/SRU_Train/Skins/Skin0/Particles/SRU_Train_Base_I_TrainSteam"
        flags: u16 = 192
        buildUpTime: f32 = 1
    }
    "Characters/SRU_Train/Skins/Skin0/Particles/SRU_Train_Base_I_Glow_Wheels_Small" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                emitterName: string = "L_Wheel_Star1"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 300, 0 }
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
                            { 200, 300, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 35, -10, -25 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.5107, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.5107, 0, 0 }
                            { 1, 0.5107, 0, 1 }
                            { 1, 0.5107, 0, 1 }
                            { 1, 0.5107, 0, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                    0x3bf176bc: u8 = 2
                }
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
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
                            { 20, 20, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0, 0 }
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Base_dian151.Milkshake_Env.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.05, 0.05 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                emitterName: string = "R_Wheel_Star1"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -200, 300, 0 }
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
                            { -200, 300, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -35, -10, -25 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.5107, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.5107, 0, 0 }
                            { 1, 0.5107, 0, 1 }
                            { 1, 0.5107, 0, 1 }
                            { 1, 0.5107, 0, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                    0x3bf176bc: u8 = 2
                }
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
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
                            { 20, 20, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0, 0 }
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Base_dian151.Milkshake_Env.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.05, 0.05 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                emitterName: string = "L_Wheel_Crystals1"
                importance: u8 = 1
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 300, 0 }
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
                            { 200, 300, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 35, -10, -25 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.4314, 0.9294, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.4314, 0.9294, 1, 0 }
                            { 0.4314, 0.9294, 1, 1 }
                            { 0.4314, 0.9294, 1, 1 }
                            { 0.4314, 0.9294, 1, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                    0x3bf176bc: u8 = 2
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
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
                            { 10, 20, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0, 0 }
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Base_Snowflake_01.Milkshake_Env.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                emitterName: string = "R_Wheel_Crystals1"
                importance: u8 = 1
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -200, 300, 0 }
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
                            { -200, 300, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -35, -10, -25 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.4314, 0.9294, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.4314, 0.9294, 1, 0 }
                            { 0.4314, 0.9294, 1, 1 }
                            { 0.4314, 0.9294, 1, 1 }
                            { 0.4314, 0.9294, 1, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                    0x3bf176bc: u8 = 2
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
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
                            { 10, 20, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0, 0 }
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Base_Snowflake_01.Milkshake_Env.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                emitterName: string = "L_Wheel_Stones1"
                importance: u8 = 1
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 600, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0
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
                            { 100, 600, 100 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -2200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -2200, 0 }
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 35, -10, -25 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.4039, 0.8609, 1, 1 }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 15, 15 }
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
                        }
                        values: list[vec3] = {
                            { 10, 15, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0825
                            0.2037
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.5963, 0.5727, 0.5727 }
                            { 0.8704, 0.8761, 0.8761 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/snow_chunks.Milkshake_Env.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                emitterName: string = "R_Wheel_Stones1"
                importance: u8 = 1
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 600, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    0
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
                            { 100, 600, 100 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -2200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -2200, 0 }
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -35, -10, -25 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.4039, 0.8609, 1, 1 }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 15, 15 }
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
                        }
                        values: list[vec3] = {
                            { 10, 15, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0825
                            0.2037
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.5963, 0.5727, 0.5727 }
                            { 0.8704, 0.8761, 0.8761 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/snow_chunks.Milkshake_Env.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.7
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
                            0.7
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "L_Wheel_Smoke1"
                importance: u8 = 1
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 100, 0 }
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
                                    0.2
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 120, 100, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    3
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
                        }
                        values: list[vec3] = {
                            { 3, 3, 3 }
                        }
                    }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 5, 0 }
                        }
                    }
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
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 35, -10, -25 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.5137, 0.8196, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.4
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 10
                }
                isUniformScale: flag = true
                isRotationEnabled: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 27, 150, 150 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.65
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 27, 150, 150 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.2, 1.2, 0 }
                            { 1.7, 1.7, 1.7 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_2x2_Smoke_Soft.Milkshake_Env.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Cloud_Pattern.Milkshake_Env.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.5, 0.5 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.7
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
                            0.7
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "R_Wheel_Smoke1"
                importance: u8 = 1
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 100, 0 }
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
                                    0.2
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 120, 100, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    3
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
                        }
                        values: list[vec3] = {
                            { 3, 3, 3 }
                        }
                    }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 5, 0 }
                        }
                    }
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
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -35, -10, -25 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.5137, 0.8196, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.4
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 10
                }
                isUniformScale: flag = true
                isRotationEnabled: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 27, 150, 150 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.65
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 27, 150, 150 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.2, 1.2, 0 }
                            { 1.7, 1.7, 1.7 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_2x2_Smoke_Soft.Milkshake_Env.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Cloud_Pattern.Milkshake_Env.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.5, 0.5 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "L_Wheel_Glow_add2"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 38, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_cylinder.Milkshake_Env.scb"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/DefaultColorOverlifetime.Milkshake_Env.tex"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.2392, 0.898, 1, 1 }
                }
                pass: i16 = 800
                censorModulateValue: vec4 = { 1, 1, 1, 0.5 }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 88 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.2, 0.1, 0.2 }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_MeshMult.Milkshake_Env.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Noise02.Milkshake_Env.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, -1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "R_Wheel_Glow_add2"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -37.5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_cylinder.Milkshake_Env.scb"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/DefaultColorOverlifetime.Milkshake_Env.tex"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.2392, 0.8986, 1, 1 }
                }
                pass: i16 = 800
                censorModulateValue: vec4 = { 1, 1, 1, 0.5 }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -88 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.2, 0.1, 0.2 }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_MeshMult.Milkshake_Env.tex"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.05 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Noise02.Milkshake_Env.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -1, -1 }
                    }
                }
            }
        }
        particleName: string = "SRU_Train_Base_I_Glow_Wheels_Small"
        particlePath: string = "Characters/SRU_Train/Skins/Skin0/Particles/SRU_Train_Base_I_Glow_Wheels_Small"
        flags: u16 = 198
    }
    "Characters/SRU_Train/Skins/Skin0/Particles/SRU_Train_Base_I_Glow_Wheels" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                emitterName: string = "L_Wheel_Star1"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 300, 0 }
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
                            { 200, 300, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 35, -28, -25 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.5107, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.5107, 0, 0 }
                            { 1, 0.5107, 0, 1 }
                            { 1, 0.5107, 0, 1 }
                            { 1, 0.5107, 0, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                    0x3bf176bc: u8 = 2
                }
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
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
                            { 20, 20, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0, 0 }
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Base_dian151.Milkshake_Env.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.05, 0.05 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                emitterName: string = "R_Wheel_Star1"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -200, 300, 0 }
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
                            { -200, 300, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -35, -28, -25 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.5107, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.5107, 0, 0 }
                            { 1, 0.5107, 0, 1 }
                            { 1, 0.5107, 0, 1 }
                            { 1, 0.5107, 0, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                    0x3bf176bc: u8 = 2
                }
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
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
                            { 20, 20, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0, 0 }
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Base_dian151.Milkshake_Env.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.05, 0.05 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                emitterName: string = "L_Wheel_Crystals1"
                importance: u8 = 1
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 300, 0 }
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
                            { 200, 300, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 35, -28, -25 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.4314, 0.9294, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.4314, 0.9294, 1, 0 }
                            { 0.4314, 0.9294, 1, 1 }
                            { 0.4314, 0.9294, 1, 1 }
                            { 0.4314, 0.9294, 1, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                    0x3bf176bc: u8 = 2
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
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
                            { 10, 20, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0, 0 }
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Base_Snowflake_01.Milkshake_Env.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                emitterName: string = "R_Wheel_Crystals1"
                importance: u8 = 1
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -200, 300, 0 }
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
                            { -200, 300, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -35, -28, -25 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.4314, 0.9294, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.4314, 0.9294, 1, 0 }
                            { 0.4314, 0.9294, 1, 1 }
                            { 0.4314, 0.9294, 1, 1 }
                            { 0.4314, 0.9294, 1, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                    0x3bf176bc: u8 = 2
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
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
                            { 10, 20, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0, 0 }
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Base_Snowflake_01.Milkshake_Env.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                emitterName: string = "L_Wheel_Stones1"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 600, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0
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
                            { 100, 600, 100 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -2200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -2200, 0 }
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 35, -10, -25 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.4039, 0.8609, 1, 1 }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 15, 15 }
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
                        }
                        values: list[vec3] = {
                            { 10, 15, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0825
                            0.2037
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.5963, 0.5727, 0.5727 }
                            { 0.8704, 0.8761, 0.8761 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/snow_chunks.Milkshake_Env.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                emitterName: string = "R_Wheel_Stones1"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 600, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    0
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
                            { 100, 600, 100 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -2200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -2200, 0 }
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -35, -10, -25 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.4039, 0.8609, 1, 1 }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 15, 15 }
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
                        }
                        values: list[vec3] = {
                            { 10, 15, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0825
                            0.2037
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.5963, 0.5727, 0.5727 }
                            { 0.8704, 0.8761, 0.8761 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/snow_chunks.Milkshake_Env.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.8
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.8
                        }
                    }
                }
                emitterName: string = "Steam_Add1"
                importance: u8 = 1
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 550, 0 }
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
                                    0.4
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 120, 550, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    3
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
                        }
                        values: list[vec3] = {
                            { 3, 3, 3 }
                        }
                    }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 5, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
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
                SpawnShape: pointer = VfxShapeCylinder {
                    height: f32 = 20
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -10, -20 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.48, 0.91, 1, 0.4 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
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
                        values: list[vec4] = {
                            { 0.48, 0.91, 1, 0.4 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.15
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 10
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0
                                0.5
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.25
                    erosionFeatherOut: f32 = 0.25
                    erosionMapName: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Base_Z_SmokeErode.Milkshake_Env.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isUniformScale: flag = true
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
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -90
                                    90
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -20
                                    20
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
                    constantValue: vec3 = { 100, 60, 1.5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.7
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
                            { 100, 60, 1.5 }
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
                            { 0.05, 0, 0 }
                            { 1.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_2x2_Smoke_Soft.Milkshake_Env.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Cloud_Pattern.Milkshake_Env.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.7
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
                            0.7
                        }
                    }
                }
                emitterName: string = "L_Wheel_Smoke1"
                importance: u8 = 1
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 100, 0 }
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
                                    0.2
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 120, 100, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    3
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
                        }
                        values: list[vec3] = {
                            { 3, 3, 3 }
                        }
                    }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 5, 0 }
                        }
                    }
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
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 35, -10, -25 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.5137, 0.8196, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.5 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.5 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 10
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 27, 150, 150 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.65
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 27, 150, 150 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.2, 1.2, 0 }
                            { 1.7, 1.7, 1.7 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_2x2_Smoke_Soft.Milkshake_Env.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Cloud_Pattern.Milkshake_Env.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.5, 0.5 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.7
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
                            0.7
                        }
                    }
                }
                emitterName: string = "R_Wheel_Smoke1"
                importance: u8 = 1
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 100, 0 }
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
                                    0.2
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 120, 100, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    3
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
                        }
                        values: list[vec3] = {
                            { 3, 3, 3 }
                        }
                    }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 5, 0 }
                        }
                    }
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
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -35, -10, -25 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.5143, 0.8205, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.5 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.5 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 10
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 27, 150, 150 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.65
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 27, 150, 150 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.2, 1.2, 0 }
                            { 1.7, 1.7, 1.7 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_2x2_Smoke_Soft.Milkshake_Env.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Cloud_Pattern.Milkshake_Env.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.5, 0.5 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "L_Wheel_Glow_add2"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 37, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_cylinder.Milkshake_Env.scb"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/DefaultColorOverlifetime.Milkshake_Env.tex"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.2392, 0.898, 1, 1 }
                }
                pass: i16 = 800
                censorModulateValue: vec4 = { 1, 1, 1, 0.5 }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 95 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.294, 0.065, 0.294 }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_MeshMult.Milkshake_Env.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Noise02.Milkshake_Env.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, -0.1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "R_Wheel_Glow_add2"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -29, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_cylinder.Milkshake_Env.scb"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/DefaultColorOverlifetime.Milkshake_Env.tex"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.2392, 0.8986, 1, 1 }
                }
                pass: i16 = 800
                censorModulateValue: vec4 = { 1, 1, 1, 0.5 }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 85 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.294, 0.065, 0.294 }
                }
                texture: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_MeshMult.Milkshake_Env.tex"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.05 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Train/Skins/Base/Particles/SRU_Train_Noise02.Milkshake_Env.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, -0.1 }
                    }
                }
            }
        }
        particleName: string = "SRU_Train_Base_I_Glow_Wheels"
        particlePath: string = "Characters/SRU_Train/Skins/Skin0/Particles/SRU_Train_Base_I_Glow_Wheels"
        flags: u16 = 198
    }
    0x643f504c = ResourceResolver {
        resourceMap: map[hash,link] = {
            "SRU_Train_I_TrainSteam" = "Characters/SRU_Train/Skins/Skin0/Particles/SRU_Train_Base_I_TrainSteam"
            0xe7da5739 = 0x5f35350b
            "SRU_Train_I_Glow_Wheels" = "Characters/SRU_Train/Skins/Skin0/Particles/SRU_Train_Base_I_Glow_Wheels"
            "SRU_Train_I_Glow_Wheels_Small" = "Characters/SRU_Train/Skins/Skin0/Particles/SRU_Train_Base_I_Glow_Wheels_Small"
            0x21ac1b2d = 0x8de333eb
            0x627afd61 = 0x58a0034f
            0x46e63955 = 0xaeb2c527
            0x8e723344 = 0x6f9a1e0e
        }
    }
}
