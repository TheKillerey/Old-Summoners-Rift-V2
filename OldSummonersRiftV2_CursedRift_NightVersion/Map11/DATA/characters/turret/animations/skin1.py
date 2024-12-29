#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Turret/Animations/Skin0" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Idle1" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/base/animations/RedHqTower_Idle.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "ShowBase" = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "SRUAP_OrderTurret1_Mat"
                        }
                        mName: hash = "ShowBase"
                    }
                }
                mFlags: u32 = 1
            }
            "State3" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/base/animations/RedHqTower_Idle.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideBase" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_OrderTurret1_Mat"
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
                }
            }
            "Destroyed" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/base/animations/RedHqTower_Idle.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xdb7fa455 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Stage2"
                        }
                        mName: hash = 0xdb7fa455
                    }
                    0xd87f9f9c = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Stage1"
                        }
                        mName: hash = 0xd87f9f9c
                    }
                    "HideBase" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_OrderTurret1_Mat"
                        }
                        mName: hash = "HideBase"
                    }
                    0x3aefb0eb = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Stage3"
                        }
                        mName: hash = 0x3aefb0eb
                    }
                }
                mFlags: u32 = 2
            }
            0xaa006aba = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Destroyed"
                }
            }
            0xcc2030a0 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/base/animations/RedHqTower_Idle.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Break1" = ParticleEventData {
                        mEffectKey: hash = "SRU_OrderTurret1_break1"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Root_break"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mName: hash = "Break1"
                    }
                    "HideBase" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_OrderTurret1_Mat"
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
                }
                mFlags: u32 = 8
            }
            "State2" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/base/animations/RedHqTower_Idle.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideBase" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_OrderTurret1_Mat"
                        }
                        mName: hash = "HideBase"
                    }
                    0x3cefb411 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Stage1"
                        }
                        mName: hash = 0x3cefb411
                    }
                }
            }
            0xf5c65fef = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/base/animations/RedHqTower_Idle.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Break2" = ParticleEventData {
                        mEffectKey: hash = "SRU_OrderTurret1_break2"
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
                            "SRUAP_OrderTurret1_Mat"
                        }
                        mName: hash = "HideBase"
                    }
                    0x3cefb411 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Stage1"
                        }
                        mName: hash = 0x3cefb411
                    }
                }
                mFlags: u32 = 8
            }
            0x5fe86160 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/base/animations/RedHqTower_Idle.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Break3" = ParticleEventData {
                        mEffectKey: hash = "SRU_OrderTurret1_break3"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Root_break"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mName: hash = "Break3"
                    }
                    "HideBase" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_OrderTurret1_Mat"
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
                    0x3aefb0eb = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Stage3"
                        }
                        mName: hash = 0x3aefb0eb
                        mStartFrame: f32 = 40
                    }
                    0xdb7fa455 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "Stage2"
                        }
                        mName: hash = 0xdb7fa455
                        mStartFrame: f32 = 40
                    }
                }
                mFlags: u32 = 8
            }
            0xa9522ec4 = SequencerClipData {
                mClipNameList: list[hash] = {
                    0xf5c65fef
                    "State3"
                }
                mFlags: u32 = 8
            }
        }
        mTrackDataMap: map[hash,embed] = {
            "Default" = TrackData {}
        }
        mBlendDataTable: map[u64,pointer] = {
            5395870133658975052 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870134011715936 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870135050951686 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870135827312800 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870136526069743 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870136587709068 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870136604486687 = TimeBlendData {
                mTime: f32 = 0
            }
            6910880694401104716 = TimeBlendData {
                mTime: f32 = 0
            }
            6910880694753845600 = TimeBlendData {
                mTime: f32 = 0
            }
            6910880695793081350 = TimeBlendData {
                mTime: f32 = 0
            }
            6910880696569442464 = TimeBlendData {
                mTime: f32 = 0
            }
            6910880697268199407 = TimeBlendData {
                mTime: f32 = 0
            }
            6910880697329838732 = TimeBlendData {
                mTime: f32 = 0
            }
            6910880697346616351 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364253485136716 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364253837877600 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364254877113350 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364255653474464 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364256352231407 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364256413870732 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364256430648351 = TimeBlendData {
                mTime: f32 = 0
            }
            14708809848001264460 = TimeBlendData {
                mTime: f32 = 0
            }
            14708809848354005344 = TimeBlendData {
                mTime: f32 = 0
            }
            14708809849393241094 = TimeBlendData {
                mTime: f32 = 0
            }
            14708809850169602208 = TimeBlendData {
                mTime: f32 = 0
            }
            14708809850868359151 = TimeBlendData {
                mTime: f32 = 0
            }
            14708809850929998476 = TimeBlendData {
                mTime: f32 = 0
            }
            14708809850946776095 = TimeBlendData {
                mTime: f32 = 0
            }
            17709948066039200588 = TimeBlendData {
                mTime: f32 = 0
            }
            17709948066391941472 = TimeBlendData {
                mTime: f32 = 0
            }
            17709948067431177222 = TimeBlendData {
                mTime: f32 = 0
            }
            17709948068207538336 = TimeBlendData {
                mTime: f32 = 0
            }
            17709948068906295279 = TimeBlendData {
                mTime: f32 = 0
            }
            17709948068967934604 = TimeBlendData {
                mTime: f32 = 0
            }
            17709948068984712223 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686951061715788 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686951414456672 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686952453692422 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686953230053536 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686953928810479 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686953990449804 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686954007227423 = TimeBlendData {
                mTime: f32 = 0
            }
            18046746275971464012 = TimeBlendData {
                mTime: f32 = 0
            }
            18046746276324204896 = TimeBlendData {
                mTime: f32 = 0
            }
            18046746277363440646 = TimeBlendData {
                mTime: f32 = 0
            }
            18046746278139801760 = TimeBlendData {
                mTime: f32 = 0
            }
            18046746278838558703 = TimeBlendData {
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
