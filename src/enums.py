from enum import Enum

class WeaponIcon(Enum):
    R99 = "https://www.apexdata.gg/assets/weapons/webp/small/r-99-77079a95406dfdafc015c04be00aefc3b5006502ab392493df924960bdc00e8b.webp"
    ALTERNATOR = "https://www.apexdata.gg/assets/weapons/webp/small/alternator-cad5827bd13cda205fc79d2245c030a38d483d9c65680001bc755b177037cc33.webp"
    PROWLER = "https://www.apexdata.gg/assets/weapons/webp/small/prowler-782f5edc3135f57fcaf952090371a27eccd7f8750d54602106956380857b1214.webp"
    FLATLINE ="https://www.apexdata.gg/assets/weapons/webp/small/flatline-621751afc0390c712148552324c15864ee4b56a50565649405b5795f554d4624.webp"
    HEMLOK = "https://www.apexdata.gg/assets/weapons/webp/small/hemlok-d9710825c20cc100f3c09c2ac6bcee09d8d06c595eba376491fa07f845ec60c9.webp"
    R301 = "https://www.apexdata.gg/assets/weapons/webp/small/r-301-22d0f7146e0664513a920db53613a2769427ff56a50cc7bc2353b2d2547a92a0.webp"
    HAVOC = "https://www.apexdata.gg/assets/weapons/webp/small/havoc-20b35048bc7c76d3fb16fa9de8a761c5f812a7b1f49616c5893e2d6268abf105.webp"
    SPITFIRE = "https://www.apexdata.gg/assets/weapons/webp/small/spitfire-38b13f7f2e5be4864bb3dcffc1501036ec349765218556cfc0da7fb946a3b333.webp"
    DEVOTION = "https://www.apexdata.gg/assets/weapons/webp/small/devotion-5a8a8afaa7e81266267c4fe75052fcfd2eda952036e933430a09ef7371cc5874.webp"
    LSTAR = "https://www.apexdata.gg/assets/weapons/webp/small/l-star-39c865455fafa9d5292012f1ee01a0a8c7e8b353ec75c73e6a556715b708a7a3.webp"
    RE45 = "https://www.apexdata.gg/assets/weapons/webp/small/re-45-c408e6cad682afc2b2f1838efa50eccc0a5a2b16ffba954ca922f0690283d63e.webp"
    P2020 = "https://www.apexdata.gg/assets/weapons/webp/small/p2020-1d6753d3e4e9eb4b422ec4a3777a809166600ead1651b05acbfdbcddcd99e82a.webp"
    WINGMAN = "https://www.apexdata.gg/assets/weapons/webp/small/wingman-3a0d3bb1436027cfc7910277467002c8d8b352a2ee52c1130831793cd7ee75db.webp"
    MOZAMBIQUE = "https://www.apexdata.gg/assets/weapons/webp/small/mozambique-df058be14205aa479b04ad0f60546d5b2ab2c33ad0bbf626a8502e059ea21e46.webp"
    PEACEKEEPER = "https://www.apexdata.gg/assets/weapons/webp/small/peacekeeper-ab276e4abb4eac6fc825719b0bb61aafa41c2b8eba9c05a39c9ac3be22a74974.webp"
    EVA8AUTO = "https://www.apexdata.gg/assets/weapons/webp/small/eva-8_auto-d4137909ee35164db3f341119621c294a54dfb74e1d2e0cca1694488a9b4c946.webp"
    MASTIFF = "https://www.apexdata.gg/assets/weapons/webp/small/mastiff-40596699146d1e19e428c9048580dca25d89e08eaff1d2c1b05134bd108b5901.webp"
    G7SCOUT = "https://www.apexdata.gg/assets/weapons/webp/small/g7_scout-f34c6f29ff7cfa4ad2a2d001705b11fffd0f4702ff54152d8a5672a046df9bb0.webp"
    LONGBOW = "https://www.apexdata.gg/assets/weapons/webp/small/longbow-294d1b921bc06d7b127be4e2396ee4133907472def9ea8066cd88674413dd102.webp"
    TRIPLETAKE = "https://www.apexdata.gg/assets/weapons/webp/small/triple_take-f8cf7047a5ee4f0c6941099bf26931946dce555830dbbc528870bc609a2ee6fd.webp"
    KRABER = "https://www.apexdata.gg/assets/weapons/webp/small/kraber-a2b62386fcc6d6598be41ac3a34f9077873ba51e8efb2979173493148953e244.webp"
    CHARGERRIFLE = "https://www.apexdata.gg/assets/weapons/webp/small/charge_rifle-dcfb49309a12e895af97fc1398cf224cfaf4c205ec223d00915c277610236926.webp"
    FRAGGRENADE = "https://www.apexdata.gg/assets/grenades/frag_grenade-8c705e5216b06fa37f6c06bc5b9844a4a68d24880e264e8c9bb27496f671043b.png"
    THERMITEGRENADE = "https://www.apexdata.gg/assets/grenades/thermite_grenade-a6897e7ccd77365867e20a15316d880676c4260eb6809f5e55eb78140f159e90.png"
    ARCSTAR = "https://www.apexdata.gg/assets/grenades/arc_star-22dc23fef8a7b52eabaf5b35499f8fc0263a8476a8ad6e17523bcdc374c54554.png"
    def __str__(self):
        return f'{self.value}'

class AmmoType(Enum):
    LIGHT = "https://www.apexdata.gg/assets/ammo_types/light-e4e2fe9d0f62b6d3f08ba9681462ce41873598ec86eccdb3897adbfda46ae657.png"
    HEAVY = "https://www.apexdata.gg/assets/ammo_types/heavy-08f9172ff7a00fe67900d3319df9b137abb3b19075e35946ca0e533f8b841195.png"
    ENERGY = "https://www.apexdata.gg/assets/ammo_types/energy-73f55cf33da115ff380d3aaf5d3de9186fbefdf1418883d3bd4f889157717bfe.png"
    SHOTGUN = "https://www.apexdata.gg/assets/ammo_types/shotgun-e0982d970d8c30d2bfc7f85a190828871e404c383b3c1dcb93e0d533d060ec28.png"
    UNIQUE = "https://www.apexdata.gg/assets/ammo_types/unique-456f35b666f52f6e544545e4ab04530777ca07c97a18de0dc49eba2f73c1ed23.png"
    def __str__(self):
        return f'{self.value}'

class Equipment(Enum):
    HELMET = "https://www.apexdata.gg/assets/equipment/helmet-16ce31bf11daecd78e759e885dfaffa4b38795395c646770657f7de611e2faf3.png"
    BODY = "https://www.apexdata.gg/assets/equipment/body_shield-90df1679d4b345f8822000082ccc705f7215c41ae4a7eaf4f8f2e60495933786.png"
    KNOCDOWNKSHIELD = "https://www.apexdata.gg/assets/equipment/knockdown_shield-9ebbc53a564867fdcb7783382ba3f0f71261aceaf9903f74a0ccacf05a9b0532.png"
    BACKPACK = "https://www.apexdata.gg/assets/equipment/backpack-feb7b18e30abcf360ee15f094e74bba84f30adc9832711dd1bb48282e8b5190e.png"
    def __str__(self):
        return f'{self.value}'


if __name__ == "__main__":
    print(getattr(WeaponIcon, "frag-grenade".replace("-", "").upper()))