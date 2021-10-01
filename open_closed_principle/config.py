from specification import OSSpecification, SizeSpecification, ProcessorSpecification, AndSpecification, OrSpecification

ANDROID = 'android'
IOS = 'ios'

SMALL = 'small'
LARGE = 'large'

SD = 'snapdragon'
MTK = 'mediatek'
BIONIC = 'bionic'

SINGLE = 'single'
AND = 'and'
OR = 'or'

SPECIFICATION_OBJ_MAP = {
    ANDROID: OSSpecification,
    IOS: OSSpecification,
    SMALL: SizeSpecification,
    LARGE: SizeSpecification,
    SD: ProcessorSpecification,
    MTK: ProcessorSpecification,
    BIONIC: ProcessorSpecification,
    SINGLE: AndSpecification,
    AND: AndSpecification,
    OR: OrSpecification
}
