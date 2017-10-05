# Digital Life Collective Project Registration

Our goal is to have a transparent and traceable method for projects that want to put themselves on the Digital Life Collective [map](https://kumu.io/DigitalLife/digital-life-collective). 

To make this easy for projects and to give you some visibility into the process we have adopted a simple github based approach that follows these steps:

 * Clone or create a simple JSON file
 * Add your details
 * Submit a pull request with the project JSON file
 * Members will review the project and approve the pull request
 * The map "build" will pick up the new information and you are on the map!


There is no other database or repository for the data and it remains source controled in github with version history for members and interested members to see. We are using the MIT license which means others can use this data.

In the review process we will do the following:

 * Check out the the project and the goals and make sure we have the right information
 * Verify the information is correct
 * Make sure it is aligned with the collective puprpose
 * Add additional fields including date, status, and tags to make it easier to filter and find.

## JSON Structure
This is a simple JSON strucuture that captures the information that will be used to generate the project map and other tools to curate the projects aligned with the Digital Life Collective.


```
{
   "project":"Digital Life Collective",
   "website":"https://diglife.com",
   "description":"The Digital Life Collective develops, funds and supports technologies created with only the individual's needs in mind.",
  "tags":[
      "collective",
      "co-op"
   ],
  "type":[
      "social media",
      "publishing"
   ],
   "purpose":[
      "privacy",
      "trust"
   ],
   "license":[
      "MIT",
      "Apache 2"
   ],
   "repoURL":"https://github.com/orgs/DigitalLifeCollective",
   "logoURL":"https://diglife.com/images/logo.png",
   "twitter":"@digitallifecollective",
   "email":"info@diglife.com",
   "techDetails":{
      "languages":[
         "python",
         "java"
      ],
      "platforms":[
         "mattermost",
         "ghost"
      ],
      "documentationLanguages":[
         "english",
         "german"
      ]
   }
}
```
