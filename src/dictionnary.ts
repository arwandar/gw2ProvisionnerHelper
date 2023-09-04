const dictionary = [
  {
    nearestWaypoint: "Commodore's Quarter Waypoint",
    nearestWaypointCode: "[&BAwEAAA=]",
    provisionner: "Skritt Trader",
    onePerTab: false,
    tabs: [
      [
        {
          tokenName: "Mystic Forge Stone",
          resourceList: [
            {
              item: "Mystic Forge Stone",
              oneADay: true,
              quantity: "1",
              price: "50 Gems",
            },
          ],
        },
        {
          tokenName: "Ectoplasm",
          resourceList: [
            {
              item: "Ectoplasm",
              id: "19721",
              oneADay: true,
              quantity: "5",
            },
          ],
        },
      ],
    ],
  },
  {
    nearestWaypoint: "Diessa Gate Waypoint",
    nearestWaypointCode: "[&BKgDAAA=]",
    provisionner: "Ash Legion Provisioner",
    onePerTab: false,
    tabs: [
      [
        {
          tokenName: "Obsidian Shard",
          oneADay: true,
          resourceList: [
            {
              item: "Obsidian Shard",
              quantity: "1",
              price: "2 100 Karma",
            },
          ],
        },
        { tokenName: "Large Skull", resourceList: [] },
      ],
    ],
  },
];

export default dictionary;
