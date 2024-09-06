#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Inhibitor/Animations/Skin2" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Idle_Normal1" = AtomicClipData {
                mFlags: u32 = 2
                mMaskDataName: hash = "base"
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Idle" = ParticleEventData {
                        mName: hash = "Audio_Idle"
                        mEffectName: string = "SRUAP_Chaos_Inhibitor_Idle1_soundy.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
                mTickDuration: f32 = 0.333333343
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/base/Animations/Inhibitor_idle1.anm"
                }
            }
            "Death_Base" = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = "Destroyed"
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "submesh" = SubmeshVisibilityEventData {
                        mName: hash = "submesh"
                        mShowSubmeshList: list[hash] = {
                            "Destroyed"
                        }
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_ChaosInhibitor_MAT"
                        }
                    }
                    "Audio_Death" = ParticleEventData {
                        mName: hash = "Audio_Death"
                        mEffectName: string = "SRUAP_Chaos_Inhibitor_Death_sound.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                    0x8e6b3646 = ParticleEventData {
                        mName: hash = 0x8e6b3646
                        mEffectName: string = "SRUAP_Chaos_Inhibitor_Death_Idle_sound.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsKillEvent: bool = false
                    }
                    "Particle" = ParticleEventData {
                        mEffectKey: hash = "SRUAP_Chaos_Inhibitor_Explosion"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "root"
                            }
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/base/Animations/inhibitor_idle_dead.anm"
                }
            }
            0xe4cb0f58 = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = "base"
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Spawn" = ParticleEventData {
                        mName: hash = "Audio_Spawn"
                        mEffectName: string = "SRUAP_Chaos_Inhibitor_Spawn_sound.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsKillEvent: bool = false
                    }
                }
                mTickDuration: f32 = 0.25
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/base/Animations/inhibitor_spawn.anm"
                }
            }
            "Spawn" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0xe4cb0f58
                }
            }
            "Idle1" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Idle_Hold"
                    0xe4cb0f58
                    0x78a49bc0
                }
            }
            0xc3247102 = AtomicClipData {
                mFlags: u32 = 2
                mMaskDataName: hash = "Destroyed"
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.25
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/base/Animations/inhibitor_idle_dead.anm"
                }
            }
            "death" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Death_Base"
                    0xc3247102
                }
            }
            "Idle_Hold" = AtomicClipData {
                mMaskDataName: hash = "base"
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 1.33333349
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/base/Animations/inhibitor_hold.anm"
                }
            }
            0x14f21665 = AtomicClipData {
                mFlags: u32 = 4
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "audio_respawn" = ParticleEventData {
                        mName: hash = "audio_respawn"
                        mStartFrame: f32 = 5
                        mEffectName: string = "SRUAP_Chaos_Inhibitor_Respawn_sound.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsKillEvent: bool = false
                    }
                    "submesh" = SubmeshVisibilityEventData {
                        mName: hash = "submesh"
                        mStartFrame: f32 = 295
                        mShowSubmeshList: list[hash] = {
                            "SRUAP_ChaosInhibitor_MAT"
                        }
                        mHideSubmeshList: list[hash] = {
                            "Destroyed"
                        }
                    }
                    "Vfx" = ParticleEventData {
                        mName: hash = "Vfx"
                        mEffectName: string = "SRUAP_Chaos_Inhibitor_Respawn.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "root"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mIsDetachable: bool = true
                    }
                    "Audio_Spawn" = ParticleEventData {
                        mName: hash = "Audio_Spawn"
                        mEffectName: string = "SRUAP_Chaos_Inhibitor_Spawn_sound.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/base/Animations/inhibitor_respawn.anm"
                }
            }
            "Idle_Normal2" = AtomicClipData {
                mMaskDataName: hash = "base"
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.333333343
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/base/Animations/inhibitor_idle2.anm"
                }
            }
            "Idle_Normal3" = AtomicClipData {
                mMaskDataName: hash = "base"
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.333333343
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/base/Animations/inhibitor_idle3.anm"
                }
            }
            0x78a49bc0 = SelectorClipData {
                mFlags: u32 = 2
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = "Idle_Normal1"
                        mProbability: f32 = 60
                    }
                    SelectorPairData {
                        mClipName: hash = "Idle_Normal2"
                        mProbability: f32 = 20
                    }
                    SelectorPairData {
                        mClipName: hash = "Idle_Normal3"
                        mProbability: f32 = 20
                    }
                }
            }
            "Respawn" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0x14f21665
                    "Idle_Normal1"
                }
            }
        }
        mMaskDataMap: map[hash,embed] = {
            "base" = MaskData {
                mWeightList: list[f32] = {
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            "Destroyed" = MaskData {
                mId: u32 = 1
                mWeightList: list[f32] = {
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                }
            }
        }
        mTrackDataMap: map[hash,embed] = {
            "Default" = TrackData {}
        }
        mBlendDataTable: map[u64,pointer] = {
            1509293449560356796 = TimeBlendData {
                mTime: f32 = 0
            }
            1509293449577134415 = TimeBlendData {
                mTime: f32 = 0
            }
            1509293449593912034 = TimeBlendData {
                mTime: f32 = 0
            }
            4188995922622193019 = TimeBlendData {
                mTime: f32 = 0
            }
            5971341806667724732 = TimeBlendData {
                mTime: f32 = 0
            }
            5971341806684502351 = TimeBlendData {
                mTime: f32 = 0
            }
            5971341806701279970 = TimeBlendData {
                mTime: f32 = 0
            }
            6043401131577472956 = TimeBlendData {
                mTime: f32 = 0
            }
            6043401131594250575 = TimeBlendData {
                mTime: f32 = 0
            }
            6043401131611028194 = TimeBlendData {
                mTime: f32 = 0
            }
            6115460456487221180 = TimeBlendData {
                mTime: f32 = 0
            }
            6115460456503998799 = TimeBlendData {
                mTime: f32 = 0
            }
            6115460456520776418 = TimeBlendData {
                mTime: f32 = 0
            }
            6115460459080752507 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364256212655483 = TimeBlendData {
                mTime: f32 = 0
            }
            16486287732941682620 = TimeBlendData {
                mTime: f32 = 0
            }
            16486287732958460239 = TimeBlendData {
                mTime: f32 = 0
            }
            16486287732975237858 = TimeBlendData {
                mTime: f32 = 0
            }
            16486287735535213947 = TimeBlendData {
                mTime: f32 = 0
            }
            17110474039877737851 = TimeBlendData {
                mTime: f32 = 0
            }
        }
    }
}
