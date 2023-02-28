ar = [1 ,2,3]
print(1+2+3)


SELECT
    DATE(submission_time) AS submission_date,
    COUNT(DISTINCT hacker_id) AS num_unique_hackers,
    MIN(hacker_id) AS hacker_id_with_max_submissions,
    hacker_name_with_max_submissions
FROM
    submissions
JOIN
    (
        SELECT
            DATE(submission_time) AS max_submission_date,
            COUNT(*) AS max_submissions,
            hacker_id AS hacker_id_with_max_submissions,
            hacker_name AS hacker_name_with_max_submissions
        FROM
            submissions
        JOIN
            hackers
        ON
            submissions.hacker_id = hackers.hacker_id
        WHERE
            submission_time >= '2016-03-01' AND submission_time < '2016-03-16'
        GROUP BY
            max_submission_date, hacker_id_with_max_submissions
    ) AS max_submissions_per_hacker
ON
    DATE(submission_time) = max_submission_date AND
    COUNT(*) = max_submissions AND
    hacker_id = hacker_id_with_max_submissions
JOIN
    hackers
ON
    hacker_id = hacker_id_with_max_submissions
WHERE
    submission_time >= '2016-03-01' AND submission_time < '2016-03-16'
GROUP BY
    submission_date, hacker_id_with_max_submissions, hacker_name_with_max_submissions
ORDER BY
    submission_date