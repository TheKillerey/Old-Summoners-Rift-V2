#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Turret/Animations/Skin2" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "State2" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_Idle1.anm"
                }
                mMaskDataName: hash = 0x66b411d8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideBase" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_ChaosTurret1_Mat"
                        }
                        mName: hash = "HideBase"
                    }
                    0x3cefb411 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Stage1"
                        }
                        mName: hash = 0x3cefb411
                    }
                    0x159a6826 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Cloth2"
                        }
                        mName: hash = 0x159a6826
                    }
                }
                mFlags: u32 = 2
            }
            "State3" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_Idle1.anm"
                }
                mMaskDataName: hash = 0x66b411d8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideBase" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_ChaosTurret1_Mat"
                        }
                        mName: hash = "HideBase"
                    }
                    0xd87f9f9c = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Stage1"
                        }
                        mName: hash = 0xd87f9f9c
                    }
                    0x39efaf58 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Stage2"
                        }
                        mName: hash = 0x39efaf58
                    }
                    0x159a6826 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Cloth1"
                        }
                        mName: hash = 0x159a6826
                    }
                    0x149a6693 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Cloth2"
                        }
                        mName: hash = 0x149a6693
                    }
                }
                mFlags: u32 = 2
            }
            "Destroyed" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_Idle1.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x07030a82 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Rubble"
                        }
                        mName: hash = 0x07030a82
                    }
                    "HideBase" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_ChaosTurret1_Mat"
                        }
                        mName: hash = "HideBase"
                    }
                    0xd87f9f9c = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Stage1"
                        }
                        mName: hash = 0xd87f9f9c
                    }
                    0xdb7fa455 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Stage2"
                        }
                        mName: hash = 0xdb7fa455
                    }
                    0x6d4f2733 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Cloth1"
                        }
                        mName: hash = 0x6d4f2733
                    }
                    0x149a6693 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Cloth2"
                        }
                        mName: hash = 0x149a6693
                    }
                }
                mFlags: u32 = 2
            }
            0x2e246d03 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_Idle1.anm"
                }
                mMaskDataName: hash = "cloth"
                mTrackDataName: hash = "cloth"
                mFlags: u32 = 4
            }
            0xaa006aba = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Destroyed"
                }
            }
            0xfd86c944 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_Idle1.anm"
                }
                mMaskDataName: hash = "cloth"
                mTrackDataName: hash = "cloth"
                mFlags: u32 = 4
            }
            0xcc2030a0 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_idle1_seq.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Break1" = ParticleEventData {
                        mEffectKey: hash = "SRU_ChaosTurret1_break1"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Root_break"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mIsDetachable: bool = true
                        mName: hash = "Break1"
                    }
                    "HideBase" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_ChaosTurret1_Mat"
                        }
                        mName: hash = "HideBase"
                        mStartFrame: f32 = 1
                    }
                    0x3cefb411 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Stage1"
                        }
                        mName: hash = 0x3cefb411
                        mStartFrame: f32 = 1
                    }
                    0x6d4f2733 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Cloth2"
                        }
                        mName: hash = 0x6d4f2733
                        mStartFrame: f32 = 1
                    }
                }
                mFlags: u32 = 8
            }
            0xf5c65fef = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_idle1_seq.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Break2" = ParticleEventData {
                        mEffectKey: hash = "SRU_ChaosTurret1_break2"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Root_break"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mIsDetachable: bool = true
                        mName: hash = "Break2"
                    }
                    "HideBase" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_ChaosTurret1_Mat"
                        }
                        mName: hash = "HideBase"
                    }
                    0x3cefb411 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Stage2"
                        }
                        mHideSubmeshList: list[hash] = {
                            "Stage1"
                        }
                        mName: hash = 0x3cefb411
                    }
                    0x6d4f2733 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Cloth2"
                        }
                        mName: hash = 0x6d4f2733
                    }
                    0x149a6693 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Cloth1"
                        }
                        mName: hash = 0x149a6693
                    }
                }
            }
            0x5fe86160 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_Idle1.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Break3" = ParticleEventData {
                        mEffectKey: hash = "SRU_ChaosTurret1_break3"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Root_break"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mIsDetachable: bool = true
                        mName: hash = "Break3"
                    }
                    "HideBase" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_ChaosTurret1_Mat"
                        }
                        mName: hash = "HideBase"
                    }
                    0xd87f9f9c = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Stage2"
                        }
                        mHideSubmeshList: list[hash] = {
                            "Stage1"
                        }
                        mName: hash = 0xd87f9f9c
                    }
                    0xdb7fa455 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Stage2"
                        }
                        mName: hash = 0xdb7fa455
                        mStartFrame: f32 = 33
                    }
                    0x6d4f2733 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Cloth1"
                        }
                        mName: hash = 0x6d4f2733
                    }
                    0x159a6826 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Cloth2"
                        }
                        mName: hash = 0x159a6826
                    }
                    0x07030a82 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Rubble"
                        }
                        mName: hash = 0x07030a82
                    }
                }
                mFlags: u32 = 8
            }
            0xb53c9a69 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_Turret_Chaos_Cloth_stage1.anm"
                }
                mTrackDataName: hash = "cloth"
                mFlags: u32 = 9
            }
            0xb43c98d6 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_Turret_Chaos_Cloth_stage2.anm"
                }
                mTrackDataName: hash = "cloth"
            }
            0x9cf732b1 = SelectorClipData {
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = 0x2e246d03
                        mProbability: f32 = 70
                    }
                    SelectorPairData {
                        mClipName: hash = 0xfd86c944
                        mProbability: f32 = 30
                    }
                }
                mFlags: u32 = 6
            }
            "Idle1_Base" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_Idle1.anm"
                }
                mMaskDataName: hash = 0x66b411d8
                mTrackDataName: hash = "Default"
                mFlags: u32 = 7
            }
            "Idle1" = ParallelClipData {
                mClipNameList: list[hash] = {
                    0x9cf732b1
                    "Idle1_Base"
                }
                mFlags: u32 = 7
            }
            "Attack2" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_Idle1.anm"
                }
                mMaskDataName: hash = 0x66b411d8
                mTrackDataName: hash = "Attack1"
            }
            "Attack1" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_idle1_seq.anm"
                }
                mMaskDataName: hash = 0x66b411d8
                mTrackDataName: hash = "Attack1"
            }
        }
        mMaskDataMap: map[hash,embed] = {
            0x66b411d8 = MaskData {
                mWeightList: list[f32] = {
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
            "cloth" = MaskData {
                mId: u32 = 1
                mWeightList: list[f32] = {
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
            "Attack1" = TrackData {
                mPriority: u8 = 1
            }
            "cloth" = TrackData {
                mPriority: u8 = 2
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            3324902285332737283 = TimeBlendData {
                mTime: f32 = 0
            }
            3324902285814922060 = TimeBlendData {
                mTime: f32 = 0
            }
            3324902288743656076 = TimeBlendData {
                mTime: f32 = 0
            }
            3324902288760433695 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870133176790275 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870133658975052 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870136587709068 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870136604486687 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686950579531011 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686951061715788 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686953990449804 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686954007227423 = TimeBlendData {
                mTime: f32 = 0
            }
            18046746275489279235 = TimeBlendData {
                mTime: f32 = 0
            }
            18046746275971464012 = TimeBlendData {
                mTime: f32 = 0
            }
            18046746278900198028 = TimeBlendData {
                mTime: f32 = 0
            }
            18046746278916975647 = TimeBlendData {
                mTime: f32 = 0
            }
        }
    }
}
