*Question 1*  

 
From: marissa@startup.com  
Subject:  Bad design  

Hello,  
  
Sorry to give you the kind of feedback that I know you do not want to hear, but I really hate the new dashboard design. Clearing and deleting indexes are now several clicks away. I am needing to use these features while iterating, so this is inconvenient.  
   
Thanks,  
Marissa  

  
--

Hi Marissa,

Thank you for the frank feedback. Rest assured that your feedback will be considered. Did you know that there is another way to manage your search indices? One particular method that comes to mind is using the Algolia API. Using this method allows you to manage multiple indices at once in your application. If you would like, I can send you a quick and easy code example for a supported language of your choice - Algolia currently supports PHP, Ruby, JavaScript, Python, Swift, Swift, Kotlin, Andoird, C#, Java, Golang, and Scala - otherwise, here is the link to the Algolia documentation for managing your indices: https://www.algolia.com/doc/guides/sending-and-managing-data/manage-your-indices/.

Best,
Jared

*Question 2*:   
  
From: carrie@coffee.com  
Subject: URGENT ISSUE WITH PRODUCTION!!!!  
  
Since today 9:15am we have been seeing a lot of errors on our website. Multiple users have reported that they were unable to publish their feedbacks and that an alert box with "Record is too big, please contact enterprise@algolia.com".  
  
Our website is an imdb like website where users can post reviews of coffee shops online. Along with that we enrich every record with a lot of metadata that is not for search. I am already a paying customer of your service, what else do you need to make your search work?  
  
Please advise on how to fix this. Thanks.   

  
--

Hi Carrie,

Thank you for reaching out regarding your application issues. My initial assumptions based on the alert box your users are getting is that your application has reached the max size allowed. A possible consideration worth looking at is reducing the size of the current index. You mentioned that a lot of non-search related metadata is included in each record, an easy immediate fix to the max size reached issue is to remove or at least cut down the non-search related metadata. 

If this is not an option that you can address right now, I can follow up with another email regarding upgrading to a plan with a higher size limit. 

Best,
Jared

*Question 3*:   


From: marc@hotmail.com  
Subject: Error on website  
  
Hi, my website is not working and here's the error:  
  
![error message](./error.png)  
  
Can you fix it please?  

--

Hi Marc,

Thank you for including the snapshot of the error message. 
