from struct import unpack, pack

entrysize = []
entryBoneData = []

def ReadpAnim(f):
    FileSize = unpack(">I", f.read(4))[0]
    fourthousandnintysix = unpack(">H", f.read(2))[0]
    unk = unpack(">H", f.read(2))[0]
    framerate = unpack(">f", f.read(4))[0]
    boneCount = unpack("B", f.read(1))[0]
    type1 = unpack("B", f.read(1))[0]
    type2 = unpack("B", f.read(1))[0]
    type3 = unpack("B", f.read(1))[0]

    for i in range(boneCount):
        fourthousandnintysix_off = unpack(">H", f.read(2))[0]
        bone_id = unpack(">H", f.read(2))[0]
        total_of_keyframe_id = unpack(">H", f.read(2))[0]
        size_off = unpack(">H", f.read(2))[0]
        for i in range(total_of_keyframe_id):
            fourthousandnintysix_on = unpack(">H", f.read(2))[0]
            key_index = unpack(">H", f.read(2))[0]
            unk = unpack(">H", f.read(2))[0]
            size_on = unpack(">H", f.read(2))[0]
            entrysize.append([key_index, size_on, bone_id])
    for i, entry_size in enumerate(entrysize,1):
        if entry_size[1]:
            startFrame = unpack(">f", f.read(4))[0]
            endFrame = unpack(">f", f.read(4))[0]
            bone_num = unpack("B", f.read(1))[0]
            offset_ = f.read(3)
            #16 bytes
            if offset_ == b"\x01\x00\x01":
                if entry_size[0] == 0:
                    XScale = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 1:
                    YScale = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 2:
                    ZScale = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 3:
                    XPos = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 4:
                    YPos = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 5:
                    ZPos = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 6:
                    XRot = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 7:
                    YRot = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 8:
                    ZRot = unpack(">f", f.read(4))[0]
            elif offset_ == b"\x02\x00\x01":
                pass
            elif offset_ == b"\x04\x00\x01":
                pass
            elif offset_ == b"\x04\x00\x02":
                pass
            elif offset_ == b"\x04\x00\x03":
                pass
            elif offset_ == b"\x04\x00\x04":
                if entry_size[0] == 0:
                    framerate = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 1:
                    framerate = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 2:
                    framerate = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 3:
                    framerate = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 4:
                    framerate = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 5:
                    framerate = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 6:
                    framerate = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 7:
                    framerate = unpack(">f", f.read(4))[0]
                elif entry_size[0] == 8:
                    framerate = unpack(">f", f.read(4))[0]
            elif offset_ == b"\x04\x00\x05":
                pass
            elif offset_ == b"\x04\x00\x06":
                pass
            elif offset_ == b"\x04\x00\x07":
                pass
            elif offset_ == b"\x04\x00\x08":
                pass
            elif offset_ == b"\x04\x00\x14":
                pass
        
    
