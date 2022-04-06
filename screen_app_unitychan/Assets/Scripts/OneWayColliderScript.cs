using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OneWayColliderScript : MonoBehaviour
{
    private GameObject mainPlatform;
    private Collider mainPlatformCollider;
    private void Awake()
    {
        mainPlatform = transform.parent.gameObject;
        mainPlatformCollider = mainPlatform.GetComponent<Collider>();
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.tag.Equals("Player"))
        {
            mainPlatformCollider.isTrigger = true;
        }
    }

    private void OnTriggerStay(Collider other)
    {
        if (other.tag.Equals("Player"))
        {
            mainPlatformCollider.isTrigger = true;
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.tag.Equals("Player"))
        {
            mainPlatformCollider.isTrigger = false;
        }
    }
}
